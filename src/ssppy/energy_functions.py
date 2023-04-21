import scipy


def energy_calculation(power_data):
    """
    Calculates the energy consumption in kilowatt-hours (kWh) using the input power data.

    Parameters
    ----------
    power_data : pandas.DataFrame
        The power data, which should have columns "Elapsed Days" and "Power".

    Returns
    -------
    float
        The energy consumption in kWh.
    """
    energy_watts_day = scipy.integrate.simps(
        power_data["Power"], power_data["Elapsed Days"]
    )
    energy_kWh = energy_watts_day / 1000 * 24
    return energy_kWh


def yearly_energy_output(total_energy, total_days):
    """
    Calculates the yearly energy output based on the total energy generated and total number of days.

    Parameters
    ----------
    total_energy : float
        Total energy generated.
    total_days : float
        Total number of days.

    Returns
    -------
    yearly_energy_output : float
        Yearly energy output calculated from total energy and total days.

    Notes
    -----
    This function assumes that a year is 365.25 days long, and calculates the yearly energy output by 
    scaling the total energy generated based on the proportion of the year represented by the total days.
    """
    proportion_of_year = total_days / 365.25
    yearly_energy_output = (1 / proportion_of_year) * total_energy
    return yearly_energy_output