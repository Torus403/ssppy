import numpy as np


def N_func(lat):
    """
    Calculate the radius of curvature in the prime vertical (N) for a given geodetic latitude.

    Parameters
    ----------
    lat : float
        The geodetic latitude in radians.

    Returns
    -------
    float
        The radius of curvature in the prime vertical (N) at the given geodetic latitude.
    """
    a = 6_378.137  # km
    b = 6_356.752_3142  # km
    e_2 = 1 - ((b*2) / (a*2))
    N = a / (np.sqrt(1 - e_2 * (np.sin(lat) ** 2)))
    return N


def geodetic_to_ECEF(ground_station_coords):
    """
    Convert geodetic coordinates to Earth-Centered, Earth-Fixed (ECEF) coordinates.

    Parameters
    ----------
    ground_station_coords : numpy.ndarray
        A 1-dimensional NumPy array containing the geodetic latitude, longitude, and height of a ground station,
        in degrees, degrees, and meters, respectively.

    Returns
    -------
    numpy.ndarray
        A 1-dimensional NumPy array containing the ECEF x, y, and z coordinates of the ground station, in meters.

    Notes
    -----
    This function assumes a WGS84 reference ellipsoid with semimajor axis a = 6_378.137 km and semiminor axis
    b = 6_356.752_3142 km. The ECEF coordinate system is a right-handed cartesian coordinate system centered
    at the Earth's center, with the x-axis passing through the prime meridian at the equator, the y-axis passing
    through the equator at 90 degrees east, and the z-axis passing through the north pole.
    """
    lat, lon, height = np.array(
        [ground_station_coords[0], ground_station_coords[1], ground_station_coords[2]]
    )
    lat, lon, height = np.deg2rad(lat), np.deg2rad(lon), height / 1000
    a = 6_378.137  # km
    b = 6_356.752_3142  # km
    e_2 = 1 - ((b*2) / (a*2))
    x = (N_func(lat) + height) * np.cos(lat) * np.cos(lon)
    y = (N_func(lat) + height) * np.cos(lat) * np.sin(lon)
    z = ((1 - e_2) * N_func(lat) + height) * np.sin(lat)
    ECEF_coords = np.array([x, y, z])
    return ECEF_coords


def visibility(ground_station_coords, sat_coords, min_elevation_angle):
    """
    Determines if a satellite is visible from a ground station, based on the minimum elevation angle specified.

    Parameters
    ----------
    ground_station_coords : array_like
        The ground station coordinates in [lat, lon, height] format.
    sat_coords : array_like
        The satellite coordinates in [x, y, z] ECEF format.
    min_elevation_angle : float
        The minimum elevation angle, in degrees, above which the satellite is considered visible.

    Returns
    -------
    int
        1 if the satellite is visible, 0 otherwise.

    """
    a = 6_378.137  # km
    b = 6_356.752_3142  # km
    f = 298.257_223_563  # f = 1 - b / a

    viewing_angle = np.deg2rad(90 - min_elevation_angle)  # rad

    pointA = ground_station_coords
    delta_F = np.array(
        [
            ((2 * pointA[0]) / (a**2)),
            ((2 * pointA[1]) / (a**2)),
            ((2 * pointA[2]) / (b**2)),
        ]
    )
    pointB = pointA + 1 * delta_F
    pointC = sat_coords

    AC = np.subtract(pointC, pointA)
    AB = np.subtract(pointB, pointA)
    proj = pointA + np.dot(AC, AB) / np.dot(AB, AB) * AB
    height_above_origin = np.linalg.norm(proj - pointA)

    radius_at_height_above_origin = height_above_origin * np.tan(viewing_angle)
    actual_radius = np.linalg.norm(pointC - proj)
    dot_prod_AB_AC = np.dot(AB, AC)

    if (actual_radius <= radius_at_height_above_origin) and (dot_prod_AB_AC > 0):
        F = 1  # visible
    else:
        F = 0  # not visible

    return F