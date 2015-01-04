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
    StarTimeDelta -- timedelta objects converted to Star Trek time
"""
from __future__ import absolute_import
from __future__ import division
import datetime


_MICROSECONDS_PER_YEAR = 365 * 24 * 60 * 60 * 1000000


class StarDate(datetime.date):
    """Inherits from datetime.date to convert to Star Trek time.

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
    BASE_YEAR = 2323

    def __init__(self, year, month, day):
        """Extends the __init__ of datetime.date.

        Args:
            year -- integer in the range 1 <= year <= 9999
            month -- integer in the range 1 <= month <= 12
            day -- integer in the range 1 <= day <= last day in
                given month, year

        Raises:
            ValueError -- if year, month, or day are non-integers
                or are outside their valid ranges specified above
        """
        super(StarDate, self).__init__(year, month, day)
        self.stardate = self._calculate_stardate()

    def __repr__(self):
        """Overrides datetime.date.__repr__ to return the stardate."""
        return "StarDate(%.1f)" % self.stardate

    def __sub__(self, stardate):
        """Overrides datetime.date.__sub__ to return a StarTimeDelta."""
        earth_delta = super(StarDate, self).__sub__(stardate)
        return StarTimeDelta(days=earth_delta.days,
                             seconds=earth_delta.seconds,
                             microseconds=earth_delta.microseconds)

    def _calculate_stardate(self):
        """Converts an Earth date to a Star Trek date."""
        star_year = (self.year - self.BASE_YEAR) * 1000
        first_date_of_year = datetime.date(year=self.year, month=1, day=1)
        days_elapsed_in_year = self - first_date_of_year
        star_day = days_elapsed_in_year.days / 365 * 1000
        return star_year + star_day

    @classmethod
    def from_date(cls, date):
        """Creates a StarDate instance from a datetime.date object."""
        return cls(year=date.year, month=date.month, day=date.day)


class StarTime(datetime.time):
    """Overrides datetime.time to convert to Star Trek time."""

    def __init__(self, hour=0, minute=0, second=0, microsecond=0,
                 *args, **kwargs):
        """Extends the __init__ of datetime.time.

        Args:
            hour -- integer in the range 0 <= hour < 24
            minute -- integer in the range 0 <= minute < 60
            second -- integer in the range 0 <= second < 60
            microsecond -- integer in the range 0 <= microsecond < 1000000

        Raises:
            ValueError -- if hour, minute, second, or microsecond are
                outside of their valid ranges specified above
        """
        super(StarTime, self).__init__(hour, minute, second, microsecond,
                                       *args, **kwargs)
        self.startime = self._calculate_startime()

    def __repr__(self):
        return "StarTime(%.4f)" % self.startime

    def __sub__(self, startime):
        """Overrides datetime.time.__sub__ to return a StarTimeDelta."""
        earth_delta = super(StarTime, self).__sub__(startime)
        return StarTimeDelta(seconds=earth_delta.seconds,
                             microseconds=earth_delta.microseconds)

    def _calculate_startime(self):
        """Converts an Earth time to a Star Trek time."""
        total_minutes = self.minute + self.hour * 60
        total_seconds = self.second + total_minutes * 60
        total_microseconds = self.microsecond + total_seconds * 1000000
        return total_microseconds / _MICROSECONDS_PER_YEAR * 1000

    @classmethod
    def from_time(cls, time):
        """Creates a StarTime instance from a datetime.time object."""
        return cls(hour=time.hour, minute=time.minute, second=time.second,
                   microsecond=time.microsecond)


class StarDateTime(datetime.datetime):
    """Overrides datetime.datetime to convert to Star Trek time."""

    def __init__(self, year, month, day, hour=None, minute=None,
                 second=None, microsecond=None, *args, **kwargs):
        """Extends the __init__ of datetime.

        Args:
            year -- integer in the range 1 <= year <= 9999
            month -- integer in the range 1 <= month <= 12
            day -- integer in the range 1 <= day <= last day in
                given month, year
            hour -- integer in the range 0 <= hour < 24
            minute -- integer in the range 0 <= minute < 60
            second -- integer in the range 0 <= second < 60
            microsecond -- integer in the range 0 <= microsecond < 1000000

        Raises:
            ValueError -- if year, month, day, hour, minute,
                second, or microsecond are outside of their
                valid ranges specified above
        """
        super(StarDateTime, self).__init__(year, month, day, hour,
                                           minute, second,
                                           microsecond, *args,
                                           **kwargs)
        self.stardatetime = self._calculate_stardatetime()

    def __repr__(self):
        return "StarDateTime(%.4f)" % self.stardatetime

    def __sub__(self, stardatetime):
        """Overrides datetime.datetime.__sub__ to return a StarTimeDelta."""
        earth_delta = super(StarDateTime, self).__sub__(stardatetime)
        return StarTimeDelta(days=earth_delta.days,
                             seconds=earth_delta.seconds,
                             microseconds=earth_delta.microseconds)

    def date(self):
        """Overrides datetime.date to return StarDate.

        Returns:
            StarDate object with same year, month, day
                as self.year, self.month, self.day
        """
        earth_date = super(StarDateTime, self).date()
        return StarDate.from_date(earth_date)

    def time(self):
        """Overrides datetime.time to return StarTime.

        Returns:
            StarTime object with same hour, minute,
                second, microsecond as self.hour,
                self.minute, self.second,
                self.microsecond
        """
        earth_time = super(StarDateTime, self).time()
        return StarTime.from_time(earth_time)

    def _calculate_stardatetime(self):
        """Calculates the stardatetime."""
        stardate = self.date().stardate
        startime = self.time().startime
        return stardate + startime

    @classmethod
    def from_datetime(cls, datetime_):
        """Create a StarDateTime object from a datetime object."""
        return cls(year=datetime_.year, month=datetime_.month,
                   day=datetime_.day, hour=datetime_.hour,
                   minute=datetime_.minute, second=datetime_.second,
                   microsecond=datetime_.microsecond)


class StarTimeDelta(datetime.timedelta):
    """Overrides datetime.timedelta to convert to Star Trek time.

    Overrides datetime.timedelta.__repr__ to return the
    difference in Star time rather than Earth time.

    StarTimeDelta is calculated by interpreting the timedelta
    as a fraction of an Earth year, multiplying by 1000, and
    rounding to four decimal places.
    """

    def __init__(self, *args, **kwargs):
        super(StarTimeDelta, self).__init__(*args, **kwargs)
        self.startimedelta = self._calculate_startimedelta()

    def __repr__(self):
        """Overrides datetime.timedelta__repr__ to return Star time delta."""
        return "StarTimeDelta(%.4f)" % self.startimedelta

    def _calculate_startimedelta(self):
        total_seconds = self.seconds + self.days * 24 * 60 * 60
        total_microseconds = self.microseconds + total_seconds * 1000000
        return total_microseconds / _MICROSECONDS_PER_YEAR * 1000
