from __future__ import absolute_import
from unittest import TestCase

from stardatetime import StarDate, StarDateTime, StarTime


class TestStarDate(TestCase):

    def test_stardate(self):
        stardate = StarDate(2015, 1, 1)
        self.assertEqual(stardate.stardate, -308000)

    def test_invalid_date_raises(self):
        with self.assertRaises(ValueError):
            StarDate(2015, 13, 1)


class TestStarTime(TestCase):

    def test_startime(self):
        startime = StarTime(1, 1)
        self.assertAlmostEqual(startime.startime, .1161, places=4)

    def test_invalid_time_raises(self):
        with self.assertRaises(ValueError):
            StarTime(25)


class TestStarDateTime(TestCase):

    def test_stardatetime(self):
        stardatetime_ = StarDateTime(year=2015, month=1, day=1,
                                     hour=1, minute=1)
        self.assertEqual(stardatetime_.date().stardate, -308000)
        self.assertAlmostEqual(stardatetime_.time().startime,
                               .1161, places=4)

    def test_invalid_datetime_raises(self):
        with self.assertRaises(ValueError):
            StarDateTime(2015, 13, 1)


class TestStarTimeDelta(TestCase):

    def test_startimedelta(self):
        stardatetime1 = StarDateTime(year=2015, month=1, day=1,
                                     hour=1)
        stardatetime2 = StarDateTime(year=2015, month=1, day=1,
                                     hour=2)
        delta = stardatetime1 - stardatetime2
        self.assertAlmostEqual(delta.startimedelta,
                               0 - StarTime(hour=1).startime,
                               places=4)
