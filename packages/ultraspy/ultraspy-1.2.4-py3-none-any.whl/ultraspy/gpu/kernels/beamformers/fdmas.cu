/* Actual DMAS kernel. A few options are available:
- interpolation: 0 or 1 (none or linear)
- should_average: 0 or 1 (False or True)
- transmit_method: 0, 1 or 2 (centered, negative delays or positive delays)
- rx_apodization_method: 0 or 1 (Boxcar or Tukey window)
- rx_apodization_alpha: Factor (float) for our apodization window
- emitted_aperture: If True, the aperture is computed for emission elements
  also
- compound: If True, the data is compounded through the transmissions
- reduce: If True, the data is reduced through the probe elements
*/

#define M_PI 3.14159265358979323846

#include "probe_distances.cu"
#include "aperture_ratio.cu"
#include "interpolation.cu"
#include "apodization.cu"


__device__ complex<float> multiply_and_sum_rfs(complex<float>* focused_data,
                                               int base,
                                               int nb_re,
                                               int count,
                                               int to_mean)
{
    /* Multiply And Sum the delays for RFs (Matrone).

      Input parameters:
      =================

      focused_data: The array of focused data for one pixel.

      base:         The starting index to consider for the focused data.

      nb_re:        The number of reception elements in the probe.

      count:        The number of concerned focused data.

      to_mean:      This option defines if we average the results after
                    beamforming (by the number of locally concerned elements,
                    check f_number for details). If 1, mean is performed, else
                    case, summation.
    */
    float acc = 0;
    for (int ix1 = 0; ix1 < nb_re - 1; ix1++) {
        if (focused_data[base + ix1].real() == 0.) { continue; }
        for (int ix2 = 1 + ix1; ix2 < nb_re; ix2++) {
            if (focused_data[base + ix2].real() == 0.) { continue; }
            float sij = focused_data[base + ix1].real() *
                        focused_data[base + ix2].real();
            acc += sqrt(abs(sij)) * ((sij > 0) - (sij < 0));
        }
    }

    if (to_mean == 1 && count > 0) {
        acc /= float((count * count + count) / 2.0);
    }
    return complex<float>(acc);
}


__device__ complex<float> multiply_and_sum_iqs(complex<float>* focused_data,
                                               int base,
                                               int nb_re,
                                               int count,
                                               int to_mean)
{
    /* Multiply And Sum the delays for IQs (Shen BB-DMAS).

      Input parameters:
      =================

      focused_data: The array of focused data for one pixel.

      base:         The starting index to consider for the focused data.

      nb_re:        The number of reception elements in the probe.

      count:        The number of concerned focused data.

      to_mean:      This option defines if we average the results after
                    beamforming (by the number of locally concerned elements,
                    check f_number for details). If 1, mean is performed, else
                    case, summation.
    */
    complex<float> acc = 0;
    for (int ix = 0; ix < nb_re; ix++) {
        if (focused_data[base + ix] == complex<float>(0)) { continue; }
        complex<float> angle (0, arg(focused_data[base + ix]));
        acc += complex<float>(sqrt(abs(focused_data[base + ix]))) * exp(angle);
    }

    if (to_mean == 1 && count > 0) {
        acc /= float(count * count);
    }

    return acc * acc;
}


template <class T>
__device__ void core_dmas(const T *data,
                          const int start_data_idx,
                          const int is_iq,
                          const float *emitted_probe,
                          const float *received_probe,
                          const float *emitted_thetas,
                          const float *received_thetas,
                          const float *delays,
                          const int nb_t,
                          const int nb_ee,
                          const int nb_re,
                          const int nb_ts,
                          const float sampling_freq,
                          const float central_freq,
                          const float t0,
                          const float sound_speed,
                          const float *f_number,
                          const float x,
                          const float y,
                          const float z,
                          complex<float> *focused_data,
                          complex<float> *grid,
                          const int nb_pixels,
                          const int interpolation_method,
                          const int should_average,
                          const int rx_apodization_method,
                          const float rx_apodization_alpha,
                          const int emitted_aperture,
                          const int compound,
                          const int reduce,
                          const int i)
{
    /* Delay Multiply And Sum algorithm kernel, called in parallel for each
       pixel. It does, for each transmission:
        - computes the distances between the pixel to beamform and the probe /
          distance in the meridional plane, to get the aperture ratios. If it
          is not visible by the probe element, it is skipped.
        - computes the transmissions distances, as the closest probe element to
          each pixel
        - for each element of the received probe, computes the reception
          distance. If needed, a phase rotation is performed (for I/Qs) and,
          then, we get the corresponding interpolated data
        - sum all the multiplication combinations of the root-squared elements
          (RFs), or the root-squared moduli with preserved phase (I/Qs)
        - average if required
        - restore dimensionality if I/Qs, by squaring the beamformed values

      Input parameters:
      =================

      data:                  The IQs to beamform, of shape (nb_a, nb_e, nb_t).

      start_data_idx:        The index of the first data to consider (if we are
                             working on a packet, this tells us from where to
                             expect to find the related frame).

      is_iq:                 Is set to 1 if the data are I/Qs (thus a phase
                             rotation is required).

      emitted_probe:         The positions of the elements of the emission
                             probe (three dimensional).

      received_probe:        The positions of the elements of the reception
                             probe (three dimensional).

      emitted_thetas:        The thetas of the emission probe (per cycle).

      received_thetas:       The thetas of the reception probe (per cycle).

      delays:                The array with all the delays of our emission
                             sequences.

      nb_t:                  The number of transmissions in our data.

      nb_ee:                 The number of emitted elements in the probe.

      nb_re:                 The number of received elements in the probe.

      nb_ts:                 The number of time samples.

      sampling_freq:         The sampling frequency of the acquisition.

      central_freq:          The central frequency of the probe used for the
                             acquisition.

      t0:                    The initial time of recording.

      sound_speed:           The speed of sound of the scanned medium.

      f_number:              The aperture of the probe elements. For any
                             position of the medium, (z / f_number)-width
                             enough to observe at depth z. Two-dimensional, for
                             both the lateral and elevational axes.

      x:                     The x position of the current pixel.

      y:                     The y position of the current pixel.

      z:                     The z position of the current pixel.

      focused_data:          The focused data to fill at a given pixel.

      grid:                  The grid where to store the beamformed results.

      nb_pixels:             The number of pixels in the grid.

      interpolation_method:  The interpolation method to use (can be 0 (no
                             interpolation) or 1 (linear)).

      should_average:        This option defines if we average the results
                             after beamforming (by the number of locally
                             concerned elements, check f_number for details).
                             If 1, Delay And Mean is performed, else cas, Delay
                             And Sum.

      rx_apodization_method: The apodization method at reception to apply (can
                             be either 0 (boxcar) or 1 (tukey)).

      rx_apodization_alpha:  The coefficient to provide to our apodization
                             window (if 0, no apodization).

      emitted_aperture:      Set to 1 if the emitted elements have an aperture,
                             else case, 0.

      compound:              If set to 0, will not compound along the
                             transmissions.

      reduce:                If set to 0, will not reduce along the probe
                             elements.

      i:                     The current index of the data (depends on the
                             current thread / block), has been defined in the
                             global caller.
    */
    int base_focused_data = i * nb_re;
    int dim_nb_t = compound == 1 ? 1 : nb_t;
    int dim_nb_re = reduce == 1 ? 1 : nb_re;

    int count_t = 0;
    for (int it = 0; it < nb_t; it++) {
        int base_it = it * dim_nb_re * nb_pixels;

        float transmission = 10;  // 10m for infinity
        for (int iee = 0; iee < nb_ee; iee++) {
            float e_dist_to_x, e_dist_to_y, e_dists;
            get_distances(emitted_probe, nb_t, nb_ee, it, iee, x, y, z,
                          &e_dist_to_x, &e_dist_to_y, &e_dists);

            int base = it * nb_ee + iee;
            if (emitted_aperture == 1) {
                float e_ratio = get_aperture_ratio(
                    z, e_dist_to_x, e_dist_to_y, e_dists,
                    emitted_thetas[base], f_number);
                if (abs(e_ratio) > 1) {
                    continue;
                }
            }

            transmission = min(transmission,
                               delays[base] * sound_speed + e_dists);
        }

        if (transmission >= 10) {
            continue;
        }

        int count_re = 0;
        for (int ire = 0; ire < nb_re; ire++) {
            int base_ire = ire * nb_pixels;

            float r_dist_to_x, r_dist_to_y, r_dists;
            get_distances(received_probe, nb_t, nb_re, it, ire, x, y, z,
                          &r_dist_to_x, &r_dist_to_y, &r_dists);

            int base = it * nb_re + ire;
            float r_ratio = get_aperture_ratio(
                z, r_dist_to_x, r_dist_to_y, r_dists,
                received_thetas[base], f_number);

            if (abs(r_ratio) > 1) {
                continue;
            }

            float reception = r_dists;
            float tau = (reception + transmission) / sound_speed;
            float delay = tau - t0;
            float data_idx = delay * sampling_freq;

            // Get the corresponding data
            int base_idx = start_data_idx + it * nb_re * nb_ts + ire * nb_ts;
            complex<float> tmp = interpolate(data, base_idx, data_idx, nb_ts,
                                             interpolation_method);

            if (tmp != T(0)) {
                count_re++;

                // Default to 1 for the apodization method here
                tmp *= get_apodization_weight(
                    r_ratio, rx_apodization_alpha, rx_apodization_method);

                if (is_iq == 1) {
                    // Phase rotation for IQs (does nothing if data are RFs)
                    complex<float> phase (0, 2 * M_PI * central_freq * tau);
                    tmp *= exp(phase);
                }

                // Add it to the focused data elements
                focused_data[base_focused_data + ire] += tmp;
            }
        }

        if (compound == 0) {
            if (is_iq == 1) {
                grid[base_it + i] = multiply_and_sum_iqs(
                    focused_data, base_focused_data, nb_re, count_re,
                    should_average);
            } else {
                grid[base_it + i] = multiply_and_sum_rfs(
                    focused_data, base_focused_data, nb_re, count_re,
                    should_average);
            }
            for (int ire = 0; ire < nb_re; ire++) {
                focused_data[base_focused_data + ire] = 0;
            }
            count_re = 0;
        }
        count_t += count_re;
    }

    if (compound == 1) {
        if (is_iq == 1) {
            grid[i] = multiply_and_sum_iqs(
                focused_data, base_focused_data, nb_re, count_t,
                should_average);
        } else {
            grid[i] = multiply_and_sum_rfs(
                focused_data, base_focused_data, nb_re, count_t,
                should_average);
        }
    }
}


extern "C" {
    __global__ void dmas_float(
            const float *data, const int is_iq,
            const float *emitted_probe, const float *received_probe,
            const float *emitted_thetas, const float *received_thetas,
            const float *delays,
            const int nb_t, const int nb_ee, const int nb_re, const int nb_ts,
            const float sampling_freq, const float central_freq, const float t0,
            const float sound_speed, const float *f_number,
            const float *x_coords, const float *y_coords, const float *z_coords,
            const int dim_nb_t, const int dim_nb_re,
            complex<float> *focused_data, complex<float> *grid,
            const int nb_pixels,
            const int interpolation_method, const int should_average,
            const int rx_apodization_method, const float rx_apodization_alpha,
            const int emitted_aperture, const int compound, const int reduce)
    {
        /* Caller of the "dmas" beamformer, more information in its device
           definition. It is expecting RFs (data of float type).
        */
        const int i = threadIdx.x + blockDim.x * blockIdx.x;
        if (i < nb_pixels) {
            int i_in_transmission = (int)i % (dim_nb_re * nb_pixels);
            int i_in_elements = (int)i_in_transmission % nb_pixels;
            int idx_p = (int)i_in_elements % nb_pixels;

            core_dmas(data, 0, is_iq, emitted_probe, received_probe,
                      emitted_thetas, received_thetas, delays,
                      nb_t, nb_ee, nb_re, nb_ts,
                      sampling_freq, central_freq, t0, sound_speed, f_number,
                      x_coords[idx_p], y_coords[idx_p], z_coords[idx_p],
                      focused_data, grid, nb_pixels,
                      interpolation_method, should_average,
                      rx_apodization_method, rx_apodization_alpha,
                      emitted_aperture, compound, reduce, i);
        }
    }

    __global__ void dmas_complex(
            const complex<float> *data, const int is_iq,
            const float *emitted_probe, const float *received_probe,
            const float *emitted_thetas, const float *received_thetas,
            const float *delays,
            const int nb_t, const int nb_ee, const int nb_re, const int nb_ts,
            const float sampling_freq, const float central_freq, const float t0,
            const float sound_speed, const float *f_number,
            const float *x_coords, const float *y_coords, const float *z_coords,
            const int dim_nb_t, const int dim_nb_re,
            complex<float> *focused_data, complex<float> *grid,
            const int nb_pixels,
            const int interpolation_method, const int should_average,
            const int rx_apodization_method, const float rx_apodization_alpha,
            const int emitted_aperture, const int compound, const int reduce)
    {
        /* Caller of the "dmas" beamformer, more information in its device
           definition. It is expecting I/Qs (data of complex type).
        */
        const int i = threadIdx.x + blockDim.x * blockIdx.x;
        if (i < nb_pixels) {
            int i_in_transmission = (int)i % (dim_nb_re * nb_pixels);
            int i_in_elements = (int)i_in_transmission % nb_pixels;
            int idx_p = (int)i_in_elements % nb_pixels;

            core_dmas(data, 0, is_iq, emitted_probe, received_probe,
                      emitted_thetas, received_thetas, delays,
                      nb_t, nb_ee, nb_re, nb_ts,
                      sampling_freq, central_freq, t0, sound_speed, f_number,
                      x_coords[idx_p], y_coords[idx_p], z_coords[idx_p],
                      focused_data, grid, nb_pixels,
                      interpolation_method, should_average,
                      rx_apodization_method, rx_apodization_alpha,
                      emitted_aperture, compound, reduce, i);
        }
    }

    __global__ void packet_dmas_float(
            const float *data, const int is_iq,
            const float *emitted_probe, const float *received_probe,
            const float *emitted_thetas, const float *received_thetas,
            const float *delays,
            const int nb_f, const int nb_t,
            const int nb_ee, const int nb_re, const int nb_ts,
            const float sampling_freq, const float central_freq, const float t0,
            const float sound_speed, const float *f_number,
            const float *x_coords, const float *y_coords, const float *z_coords,
            const int dim_nb_t, const int dim_nb_re,
            complex<float> *focused_data, complex<float> *grid,
            const int total_nb_pixels,
            const int interpolation_method, const int should_average,
            const int rx_apodization_method, const float rx_apodization_alpha,
            const int emitted_aperture, const int compound, const int reduce)
    {
        /* Caller of the "dmas" beamformer working on packet of data, more
           information in its device definition. It is expecting RFs (data of
           float type).
        */
        const int i = threadIdx.x + blockDim.x * blockIdx.x;
        if (i < total_nb_pixels) {
            int i_in_transmission = (int)i % (dim_nb_re * total_nb_pixels);
            int i_in_elements = (int)i_in_transmission % total_nb_pixels;
            int i_in_pixels = (int)i_in_elements % nb_f;

            int idx_p = (int)i_in_elements / nb_f;
            int idx_f = i_in_pixels;

            int data_start_idx = idx_f * nb_t * nb_re * nb_ts;

            core_dmas(data, data_start_idx, is_iq,
                      emitted_probe, received_probe,
                      emitted_thetas, received_thetas, delays,
                      nb_t, nb_ee, nb_re, nb_ts,
                      sampling_freq, central_freq, t0, sound_speed, f_number,
                      x_coords[idx_p], y_coords[idx_p], z_coords[idx_p],
                      focused_data, grid, total_nb_pixels,
                      interpolation_method, should_average,
                      rx_apodization_method, rx_apodization_alpha,
                      emitted_aperture, compound, reduce, i);
        }
    }

    __global__ void packet_dmas_complex(
            const complex<float> *data, const int is_iq,
            const float *emitted_probe, const float *received_probe,
            const float *emitted_thetas, const float *received_thetas,
            const float *delays,
            const int nb_f, const int nb_t,
            const int nb_ee, const int nb_re, const int nb_ts,
            const float sampling_freq, const float central_freq, const float t0,
            const float sound_speed, const float *f_number,
            const float *x_coords, const float *y_coords, const float *z_coords,
            const int dim_nb_t, const int dim_nb_re,
            complex<float> *focused_data, complex<float> *grid,
            const int total_nb_pixels,
            const int interpolation_method, const int should_average,
            const int rx_apodization_method, const float rx_apodization_alpha,
            const int emitted_aperture, const int compound, const int reduce)
    {
        /* Caller of the "dmas" beamformer, more information in its device
           definition. It is expecting I/Qs (data of complex type).
        */
        const int i = threadIdx.x + blockDim.x * blockIdx.x;
        if (i < total_nb_pixels) {
            int i_in_transmission = (int)i % (dim_nb_re * total_nb_pixels);
            int i_in_elements = (int)i_in_transmission % total_nb_pixels;
            int i_in_pixels = (int)i_in_elements % nb_f;

            int idx_p = (int)i_in_elements / nb_f;
            int idx_f = i_in_pixels;

            int data_start_idx = idx_f * nb_t * nb_re * nb_ts;

            core_dmas(data, data_start_idx, is_iq,
                      emitted_probe, received_probe,
                      emitted_thetas, received_thetas, delays,
                      nb_t, nb_ee, nb_re, nb_ts,
                      sampling_freq, central_freq, t0, sound_speed, f_number,
                      x_coords[idx_p], y_coords[idx_p], z_coords[idx_p],
                      focused_data, grid, total_nb_pixels,
                      interpolation_method, should_average,
                      rx_apodization_method, rx_apodization_alpha,
                      emitted_aperture, compound, reduce, i);
        }
    }
}
