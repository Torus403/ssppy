import numpy as np
import pandas


def read_sat_coords(data, index):
    """
    Construct a NumPy array containing the coordinates of a satellite from a given
    data dictionary and index.

    Parameters
    ----------
    data : dict
        A dictionary containing satellite data, with keys "DefaultSC.EarthFixed.X",
        "DefaultSC.EarthFixed.Y", and "DefaultSC.EarthFixed.Z", each of which maps to
        a 1-dimensional NumPy array of the same length.
    index : int
        The index of the satellite to extract coordinates for.

    Returns
    -------
    np.ndarray
        A 1-dimensional NumPy array of length 3, containing the X, Y, and Z coordinates
        of the satellite at the given index.
    """
    sat_coords = np.array(
        [
            data["DefaultSC.EarthFixed.X"][index],
            data["DefaultSC.EarthFixed.Y"][index],
            data["DefaultSC.EarthFixed.Z"][index],
        ]
    )
    return sat_coords


def read_sun_coords(data, index):
    """
    Construct a NumPy array containing the coordinates of the Sun from a given
    data dictionary and index.

    Parameters
    ----------
    data : dict
        A dictionary containing Sun data, with keys "Sun.EarthFixed.X",
        "Sun.EarthFixed.Y", and "Sun.EarthFixed.Z", each of which maps to
        a 1-dimensional NumPy array of the same length.
    index : int
        The index of the Sun to extract coordinates for.

    Returns
    -------
    np.ndarray
        A 1-dimensional NumPy array of length 3, containing the X, Y, and Z coordinates
        of the Sun at the given index.
    """
    sun_coords = np.array(
        [
            data["Sun.EarthFixed.X"][index],
            data["Sun.EarthFixed.Y"][index],
            data["Sun.EarthFixed.Z"][index],
        ]
    )
    return sun_coords


def read_elapsed_days(data, index):
    """
    Retrieve the elapsed days value for a satellite at a given index from a data dictionary.

    Parameters
    ----------
    data : dict
        A dictionary containing satellite data, with a key "DefaultSC.ElapsedDays" mapping to
        a 1-dimensional NumPy array of elapsed days values.
    index : int
        The index of the satellite to retrieve the elapsed days value for.

    Returns
    -------
    float
        The elapsed days value for the satellite at the given index.
    """
    elapsed_days = data["DefaultSC.ElapsedDays"][index]
    return elapsed_days