from datetime import date, datetime, time, timedelta


class StarDate(date):
    BASE_YEAR = 2323

    def __init__(self, *args, **kwargs):
        self.star_year = self._calculate_star_year()
        self.star_day = self._calculate_star_day()
        super(Stardate, self).__init__(*args, **kwargs)

    def __repr__(self):
        star_year = self._calculate_star_year()
        star_day = self._calculate_star_day()
        return str(star_year * 1000 + star_day)

    def __sub__(self, stardate):
        earth_delta = super(Stardate, self).__sub__(stardate)
        return StarTimeDelta(days=earth_delta.days,
                             seconds=earth_delta.seconds,
                             microseconds=earth_delta.microseconds)

    def _calculate_star_year(self):
        return self.year - self.BASE_YEAR

    def _calculate_star_day(self):
        day_count = self - date(year=self.year, month=1, day=1)
        return round(day_count.days / 365.0 * 1000, 1)


class StarTimeDelta(timedelta):

    def __repr__(self):
        return str(round(self.days / 365.0 * 1000, 4))
