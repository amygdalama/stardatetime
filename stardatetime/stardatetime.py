from datetime import date, datetime, time, timedelta

import conversion


class StarDate(date):
    BASE_YEAR = 2323

    def __init__(self, *args, **kwargs):
        year = kwargs.get('year', args[0])
        month = kwargs.get('month', args[1])
        day = kwargs.get('day', args[2])
        self.stardate = conversion.earth_date_to_star_date(year, month, day)
        super(StarDate, self).__init__(*args, **kwargs)

    def __repr__(self):
        return str(self.stardate)

    def __sub__(self, stardate):
        earth_delta = super(Stardate, self).__sub__(stardate)
        return StarTimeDelta(days=earth_delta.days,
                             seconds=earth_delta.seconds,
                             microseconds=earth_delta.microseconds)


class StarTimeDelta(timedelta):

    def __repr__(self):
        return str(round(self.days / 365.0 * 1000, 4))
