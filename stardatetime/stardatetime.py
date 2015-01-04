"""Main module for stardatetime.

Defines StarDate, StarTime, StarDateTime, and StarTimeDelta classes.

Star Trek time is (imperfectly) of the format YYXXX.XX, with the
first two digits representing the year, with 2323 as the base year,
and the following digits representing the percentage of the Earth
year that has passed, rounded to two decimal places.

Classes:
    StarDate -- date objects converted to Star Trek time
    StarTime -- time objects converted to Star Trek time
    StarDateTime -- datetime objects converted to Star Trek time
    StarTimeDelta -- timedelta objects converted to StarTrek time
"""
from __future__ import absolute_import
from datetime import date, datetime, time, timedelta

from stardatetime import conversion


class StarDate(date):
    """Inherits from datetime.date to convert to Star Time.

    Extends datetime.date.__init__ to add a stardate
    attribute.

    Overrides datetime.date.__repr__
    to return the stardate value, rather than the
    Earth date value.

    Overrides datetime.date.__sub__ to return a
    StarTimeDelta object rather than a
    datetime.timedelta object.

    Attributes:
        stardate -- integer representing the stardate
            associated with midnight of the date provided
    """

    def __init__(self, year, month, day):
        """Extends the __init__ of datetime.date.

        Args:
            year -- Earth year, acceptable values are integers
                between 0 and 9999
            month -- Earth month, acceptable values are integers
                between 1 and 12
            day -- Earth day, acceptable values are integers
                between 1 and the last valid day of the month

        Raises:
            ValueError -- if year, month, or day are non-integers
                or are outside their valid ranges specified above
        """
        self.stardate = conversion.earth_date_to_star_date(year, month, day)
        super(StarDate, self).__init__(year, month, day)

    def __repr__(self):
        """Overrides datetime.date.__repr__ to return the stardate."""
        return str(self.stardate)

    def __sub__(self, stardate):
        """Overrides datetime.date.__sub__ to return a StarTimeDelta."""
        earth_delta = super(StarDate, self).__sub__(stardate)
        return StarTimeDelta(days=earth_delta.days,
                             seconds=earth_delta.seconds,
                             microseconds=earth_delta.microseconds)


class StarTime(time):
    """Overrides datetime.time to convert to Star Trek time."""
    pass


class StarDateTime(datetime):
    """Overrides datetime.datetime to convert to Star Trek time."""
    pass


class StarTimeDelta(timedelta):
    """Overrides datetime.timedelta to convert to Star Time.

    Overrides datetime.timedelta.__repr__ to return the
    difference in Star time rather than Earth time.

    StarTimeDelta is calculated by interpreting the timedelta
    as a fraction of an Earth year, multiplying by 1000, and
    rounding to four decimal places.
    """

    def __repr__(self):
        """Overrides datetime.timedelta__repr__ to return Star time delta."""
        return str(round(self.days / 365.0 * 1000, 4))
