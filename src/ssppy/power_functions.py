import numpy as np


def current_power(initial_power, dist_factor, deg_factor):
    """
    Calculates the current power based on the initial power, distance factor, and degree factor.

    Parameters
    ----------
    initial_power : float
        The initial power value in watts.
    dist_factor : float
        The distance factor, which is a decimal value representing the current distance from the power source relative to
        the initial distance.
    deg_factor : float
        The degree factor, which is a decimal value representing the current degree of misalignment of the receiver
        relative to the optimal alignment.

    Returns
    -------
    float
        The current power value in watts, calculated as the product of the initial power, distance factor, and degree
        factor.
    """
    current_power = initial_power * deg_factor * dist_factor
    return current_power


def dist_factor(sat_coords, sun_coords):
    """
    Calculate the distance factor between a satellite and the Sun.

    Parameters
    ----------
    sat_coords : array_like
        The coordinates of the satellite, in km.
    sun_coords : array_like
        The coordinates of the Sun, in km.

    Returns
    -------
    float
        The distance factor, given by the distance from the satellite to the
        Sun in astronomical units (AU) divided by the distance from the Earth to
        the Sun in AU.

    Notes
    -----
    The distance factor is used to calculate the power received by the satellite
    from the Sun, assuming that the power radiated by the Sun is constant and
    that it follows an inverse-square law.
    """
    dist_sat_sun = np.linalg.norm(sun_coords - sat_coords)
    AU = 149_597_870.700
    dist_power_factor = AU / dist_sat_sun
    return dist_power_factor


def deg_factor(annual_deg_rate, elapsed_days):
    """
    Calculates the degradation factor of a system based on the annual rate of degradation and the elapsed time.

    Parameters
    ----------
    annual_deg_rate : float
        The annual rate of degradation of the system.
    elapsed_days : float
        The number of days that have elapsed since the system was installed.

    Returns
    -------
    deg_power_factor : float
        The degradation factor of the system.

    Notes
    -----
    The degradation factor is calculated using the formula (1 - daily_deg_rate) ** elapsed_days, 
    where daily_deg_rate is calculated as annual_deg_rate / 365.25.

    """
    daily_deg_rate = annual_deg_rate / 365.25
    deg_power_factor = (1 - daily_deg_rate) ** elapsed_days
    return deg_power_factor


def power_calculation(current_power, V, S):
    """
    Calculate the actual power value based on the current power, voltage, and current surface area.

    Parameters
    ----------
    current_power : float
        The current power value in watts.
    V : float
        The visibility value.
    S : float
        The shadow value.

    Returns
    -------
    float
        The actual power value in watts, calculated as current_power * V * S.
    """
    actual_power_value = current_power * V * S
    return actual_power_value