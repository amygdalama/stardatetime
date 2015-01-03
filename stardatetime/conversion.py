"""Helper functions for converting from earth time to star time."""
from datetime import date


def earth_date_to_star_date(earth_year, earth_month, earth_day):
    """Converts an Earth date to a star date.

    >>> earth_date_to_star_date(2323, 1, 1)
    0.0
    >>> earth_date_to_star_date(2015, 1, 1)
    -308000.0
    >>> earth_date_to_star_date(2014, 12, 31)
    -308002.7
    """

    star_year = (earth_year - 2323) * 1000
    first_date_of_year = date(year=earth_year, month=1, day=1)
    earth_date = date(year=earth_year, month=earth_month, day=earth_day)
    days_elapsed_in_year = earth_date - first_date_of_year
    star_day = round(days_elapsed_in_year.days / 365.0 * 1000, 1)
    return star_year + star_day
