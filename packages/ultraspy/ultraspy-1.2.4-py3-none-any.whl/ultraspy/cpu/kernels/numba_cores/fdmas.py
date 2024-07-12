"""Numba cores to compute FDMAS algorithm in an optimized way (no python).
"""
import numpy as np
from numba import njit, prange

from .aperture_ratio import get_aperture_ratio, set_to_inf
from .probe_distances import get_distances
from .interpolation import interpolate
from .apodization import get_apodization_weight


@njit(fastmath=True)
def combine_dmas(pixel_focused_data, nb_focused_data):
    """Combine RF signals using method of Matrone et al., 2014. Basically sums
    all the possible combinations of root-squared delays, with preserved signs.

    :param numpy.ndarray pixel_focused_data: The focused data for the pixel
    :param int nb_focused_data: The number of the concerned focused data for
        this pixel

    :returns: The value after DMAS of the delays
    :return type: float
    """
    acc = 0
    for ix1 in range(0, nb_focused_data - 1):
        if pixel_focused_data[ix1] == 0:
            continue
        for ix2 in range(1 + ix1, nb_focused_data):
            if pixel_focused_data[ix2] == 0:
                continue
            sij = pixel_focused_data[ix1] * pixel_focused_data[ix2]
            acc += np.sqrt(np.abs(sij)) * np.sign(sij)
    return acc


@njit(fastmath=True)
def combine_bb_dmas(pixel_focused_data, nb_focused_data):
    """Combine I/Q signals using method of Shen et al., 2019. Basically the sum
    of the root-squared moduli with preserved phase.

    :param numpy.ndarray pixel_focused_data: The focused data for the pixel
    :param int nb_focused_data: The number of the concerned focused data for
        this pixel

    :returns: The value after DMAS of the delays
    :return type: complex
    """
    acc = 0
    for ix in range(nb_focused_data):
        phase = np.angle(pixel_focused_data[ix]) * 1j
        acc += np.sqrt(np.abs(pixel_focused_data[ix])) * np.exp(phase)
    return acc


@njit(parallel=True)
def delay_multiply_and_sum(data, is_iq, emitted_probe, received_probe,
                           emitted_thetas, received_thetas, delays,
                           sampling_freq, central_freq,
                           t0, sound_speed, f_number,
                           xs, ys, zs,
                           interpolation_method, reduction_method,
                           rx_apodization_method, rx_apodization_alpha,
                           emitted_aperture, reduce, compound, is_same_probe):
    """Core code computing the Delay Multiply And Sum algorithm using Numba (in
    an iterative way). Note that it is using both the nopython and the parallel
    modes of Numba, meaning that only simple operations are available (slicing
    does not work for example). The algorithm does, for each pixel, then for
    each transmission:

        - computes the distances between the pixels to beamform and the probe /
          distance in the meridional plane, to get the aperture ratios. Pixels
          that are not visible are set to infinite. Note that if the emission
          and reception probes are the same, those are computed only once for
          all the transmissions
        - computes the transmissions distances, as the closest probe element to
          each pixel
        - for each element of the received probe, computes the reception
          distance. If needed, a phase rotation is performed (for I/Qs) and,
          then, we get the corresponding interpolated data
        - sum all the multiplication combinations of the root-squared elements
          (RFs), or the root-squared moduli with preserved phase (I/Qs)
        - average if required
        - restore dimensionality if I/Qs, by squaring the beamformed values

    :param numpy.ndarray data: The RFs or I/Qs to beamform, of shape (nb_t,
        nb_re, nb_ts)
    :param bool is_iq: If True, the data are I/Qs. RFs else case
    :param numpy.ndarray emitted_probe: The positions of the elements of the
        emitted probe, of shape (nb_t, nb_ee)
    :param numpy.ndarray received_probe: The positions of the elements of the
        received probe, of shape (nb_t, nb_re)
    :param numpy.ndarray emitted_thetas: The angles for each element of the
        emitted probe (only relevant to convex probes, none else case), of
        shape (nb_t, nb_ee)
    :param numpy.ndarray received_thetas: The angles for each element of the
        received probe (only relevant to convex probes, none else case), of
        shape (nb_t, nb_re)
    :param numpy.ndarray delays: The delays applied to each transmission, for
        each element, of shape (nb_t, nb_ee)
    :param float sampling_freq: The sampling frequency of the acquisition
    :param float central_freq: The center frequency of the probes used for the
        acquisition
    :param float t0: The initial time of recording
    :param float sound_speed: The speed of sound of the scanned medium
    :param float f_number: The aperture of the probes elements. For any position
        of the medium, (z / f_number)-width elements of the probes may have an
        aperture wide enough to observe at depth z
    :param numpy.ndarray xs: The lateral pixels coordinates, of shape (nb_p,)
    :param numpy.ndarray ys: The elevational pixels coordinates, of shape
        (nb_p,)
    :param numpy.ndarray zs: The axial pixels coordinates, of shape (nb_p,)
    :param int interpolation_method: The interpolation method to use (can be 0
        (no interpolation) or 1 (linear))
    :param int reduction_method: This option defines if we average the results
        after beamforming (by the number of locally concerned elements, check
        f_number for details). If 1, Delay And Mean is performed, else cas,
        Delay And Sum
    :param int rx_apodization_method: This option defines if we perform
        apodization on our beamformed data. The method can be either 0 (boxcar)
        or 1 (tukey)
    :param float rx_apodization_alpha: The alpha to apply for the apodization
        (only effective for the tukey apodization)
    :param int emitted_aperture: If set to 1 (True), we apply the aperture
        f-number for emitted elements
    :param int reduce: Not implemented in FDMAS, always True
    :param int compound: If set to 1 (True), we compound the data
    :param int is_same_probe: If True, the emitted and received probes are the
        same

    :returns: Beamformed grid of shape (1, 1, nb_p,). If the `compound` option
        is set to False, the transmission dimension is preserved, leading to
        the shape (nb_t, 1, nb_p). `reduce` needs to be performed using FDMAS
    :return type: numpy.ndarray
    """
    # Probes for emission / reception
    _, e_nb_elements = emitted_probe[0].shape
    nb_t, r_nb_elements = received_probe[0].shape

    e_dist2x = np.zeros(e_nb_elements)
    e_dist2y = np.zeros(e_nb_elements)
    r_dist2x = np.zeros(r_nb_elements)
    r_dist2y = np.zeros(r_nb_elements)
    e_dists = np.zeros(e_nb_elements)
    r_dists = np.zeros(r_nb_elements)

    # Reduction method based on signal type
    combine_core = combine_bb_dmas if is_iq else combine_dmas

    # Define size of grid given if we compound or not
    nb_transmissions = nb_t if compound == 0 else 1
    nb_elements = r_nb_elements if reduce == 0 else 1
    nb_pixels = xs.size
    grid = np.zeros((nb_transmissions, nb_elements, nb_pixels), np.complex64)

    for p in prange(nb_pixels):
        tmp_delays = np.zeros((r_nb_elements,), dtype=np.complex128)
        count = np.zeros((nb_transmissions, nb_elements))

        # If is same probe, the emitted and received probe are the same,
        # we compute the distances beforehand
        if is_same_probe:
            e_dist2x, e_dist2y, e_dists = get_distances(
                emitted_probe, xs[p], ys[p], zs[p])
            r_dist2x, r_dist2y, r_dists = e_dist2x, e_dist2y, e_dists

        for it in range(nb_t):
            # If not the same probe, we compute both distances
            if not is_same_probe:
                # Emission
                e_dist2x, e_dist2y, e_dists = get_distances(
                    emitted_probe, xs[p], ys[p], zs[p], transmission=it)
                # Reception
                r_dist2x, r_dist2y, r_dists = get_distances(
                    received_probe, xs[p], ys[p], zs[p], transmission=it)

            # Aperture of the received elements
            r_ratio = get_aperture_ratio(zs[p], r_dist2x, r_dist2y, r_dists,
                                         received_thetas[it], f_number)

            # If the emission also has an aperture, we set the distances
            # outside it to infinite, so they are never used
            if emitted_aperture == 1:
                e_ratio = get_aperture_ratio(zs[p], e_dist2x, e_dist2y, e_dists,
                                             emitted_thetas[it], f_number)
                e_dists = set_to_inf(e_dists, e_ratio)

            # Transmission distances
            transmission = np.inf
            for iee in range(e_nb_elements):
                transmission = min(transmission,
                                   delays[it, iee] * sound_speed + e_dists[iee])
            if transmission == np.inf:
                continue

            for ire in range(r_nb_elements):
                if np.abs(r_ratio[ire]) > 1:
                    continue

                # Reception distances
                reception = r_dists[ire]

                # Compute the delays and get the data given the chosen
                # interpolation method
                tau = (reception + transmission) / sound_speed
                delay = tau - t0
                focused_data = interpolate(delay * sampling_freq, data[it, ire],
                                           interpolation_method)

                if focused_data is not None:
                    # Sum over the transmissions and reception elements
                    iit = it if compound == 0 else 0
                    iie = ire if reduce == 0 else 0
                    count[iit, iie] += 1

                    focused_data *= get_apodization_weight(
                        r_ratio[ire], rx_apodization_alpha,
                        rx_apodization_method)

                    if is_iq:
                        focused_data *= np.exp(2j * np.pi * central_freq * tau)

                    tmp_delays[ire] += focused_data

            # If we don't compound, we perform the DMAS operation right now,
            # before next transmission
            if compound == 0:
                grid[it, 0, p] += combine_core(tmp_delays, r_nb_elements)
                tmp_delays = np.zeros((r_nb_elements,), dtype=np.complex128)

        # If we compound, we perform the DMAS operation now, after collecting
        # all the transmissions
        if compound == 1:
            grid[0, 0, p] += combine_core(tmp_delays, r_nb_elements)

        # If average, we divide by the counters
        if reduction_method == 1:
            for iit in range(nb_transmissions):
                c = count[iit, 0]
                if is_iq:
                    grid[iit, 0, p] /= (c ** 2)
                else:
                    grid[iit, 0, p] /= (c ** 2 + c) / 2

        # If BB DMAS, we need to square the final values to restore
        # dimensionality
        if is_iq:
            for iit in range(nb_transmissions):
                grid[iit, 0, p] *= grid[iit, 0, p]

    return grid


@njit
def delay_multiply_and_sum_packet(data, is_iq, emitted_probe, received_probe,
                                  emitted_thetas, received_thetas, delays,
                                  sampling_freq, central_freq, t0, sound_speed,
                                  f_number,
                                  xs, ys, zs,
                                  interpolation_method, reduction_method,
                                  rx_apodization_method, rx_apodization_alpha,
                                  emitted_aperture, reduce, compound,
                                  is_same_probe):
    """Caller to redirect to the core kernel. Iterates over a packet of frame.

    :param numpy.ndarray data: The RFs or I/Qs to beamform, of shape (nb_t,
        nb_re, nb_ts)
    :param bool is_iq: If True, the data are I/Qs. RFs else case
    :param numpy.ndarray emitted_probe: The positions of the elements of the
        emitted probe, of shape (nb_t, nb_ee)
    :param numpy.ndarray received_probe: The positions of the elements of the
        received probe, of shape (nb_t, nb_re)
    :param numpy.ndarray emitted_thetas: The angles for each element of the
        emitted probe (only relevant to convex probes, none else case), of
        shape (nb_t, nb_ee)
    :param numpy.ndarray received_thetas: The angles for each element of the
        received probe (only relevant to convex probes, none else case), of
        shape (nb_t, nb_re)
    :param numpy.ndarray delays: The delays applied to each transmission, for
        each element, of shape (nb_t, nb_ee)
    :param float sampling_freq: The sampling frequency of the acquisition
    :param float central_freq: The center frequency of the probes used for the
        acquisition
    :param float t0: The initial time of recording
    :param float sound_speed: The speed of sound of the scanned medium
    :param float f_number: The aperture of the probes elements. For any position
        of the medium, (z / f_number)-width elements of the probes may have an
        aperture wide enough to observe at depth z
    :param numpy.ndarray xs: The lateral pixels coordinates, of shape (nb_p,)
    :param numpy.ndarray ys: The elevational pixels coordinates, of shape
        (nb_p,)
    :param numpy.ndarray zs: The axial pixels coordinates, of shape (nb_p,)
    :param int interpolation_method: The interpolation method to use (can be 0
        (no interpolation) or 1 (linear))
    :param int reduction_method: This option defines if we average the results
        after beamforming (by the number of locally concerned elements, check
        f_number for details). If 1, Delay And Mean is performed, else cas,
        Delay And Sum
    :param int rx_apodization_method: This option defines if we perform
        apodization on our beamformed data. The method can be either 0 (boxcar)
        or 1 (tukey)
    :param float rx_apodization_alpha: The alpha to apply for the apodization
        (only effective for the tukey apodization)
    :param int emitted_aperture: If set to 1 (True), we apply the aperture
        f-number for emitted elements
    :param int reduce: Not implemented in FDMAS, always True
    :param int compound: If set to 1 (True), we compound the data
    :param int is_same_probe: If True, the emitted and received probes are the
        same

    :returns: Beamformed grid of shape (1, 1, nb_p, nb_f). If the `compound`
        option is set to False, the transmission dimension is preserved,
        resulting in the shape (nb_t, 1, nb_p, nbf)
    :return type: numpy.ndarray
    """
    # Could be optimized since already defined in every frame
    nb_f = data.shape[0]
    nb_t, r_nb_elements = received_probe[0].shape
    nb_transmissions = nb_t if compound == 0 else 1
    nb_elements = r_nb_elements if reduce == 0 else 1
    nb_pixels = xs.size
    grid = np.empty((nb_transmissions, nb_elements, nb_pixels, nb_f),
                    np.complex64)

    for f in range(data.shape[0]):
        grid[..., f] = delay_multiply_and_sum(
            data[f], is_iq, emitted_probe, received_probe,
            emitted_thetas, received_thetas, delays,
            sampling_freq, central_freq, t0, sound_speed, f_number,
            xs, ys, zs,
            interpolation_method, reduction_method,
            rx_apodization_method, rx_apodization_alpha, emitted_aperture,
            reduce, compound, is_same_probe)

    return grid
