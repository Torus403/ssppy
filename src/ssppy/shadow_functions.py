import numpy as np
import math


def shadow(sat_coords, sun_coords):
    """
    Determines if a satellite is in the shadow of the Earth.

    Parameters
    ----------
    sat_coords : array_like
        The position vector of the satellite in Cartesian coordinates, in kilometers.
    sun_coords : array_like
        The position vector of the Sun in Cartesian coordinates, in kilometers.

    Returns
    -------
    F : float
        The fraction of the satellite's surface area that is illuminated by the Sun, ranging from 0.0 to 1.0.
        If the satellite is completely in the Earth's shadow, returns 0.0. If the satellite is completely
        illuminated by the Sun, returns 1.0.

    Notes
    -----
    This function assumes that the Earth is an ideal sphere with radius 6,378.1 km and that the Sun is a perfect
    sphere with radius 696,340 km. It also assumes that the Sun is much farther away from the Earth than the satellite,
    and that the Earth's atmosphere does not affect the calculations.
    """
    sun_radius = 696_340  # km
    earth_radius = 6_378.1  # km

    a = np.arcsin(sun_radius / np.linalg.norm(sun_coords - sat_coords))
    b = np.arcsin(earth_radius / np.linalg.norm(sat_coords))
    c = np.arccos(
        np.dot(-sat_coords, (sun_coords - sat_coords))
        / (np.linalg.norm(sat_coords) * np.linalg.norm(sun_coords - sat_coords))
    )

    if (a + b) <= c:
        F = 1.0
    elif c <= (b - a):
        F = 0.0
    elif np.abs(a - b) < c and c < (a + b):
        x = ((c*2) + (a2) - (b*2)) / (2 * c)
        y = np.sqrt((a*2) - (x*2))
        A = (a*2) * np.arccos(x / a) + (b*2) * np.arccos((c - x) / b) - c * y
        F = 1.0 - (A / (math.pi * (a**2)))
    else:
        F = 1 - ((b*2) / (a*2))
    return F