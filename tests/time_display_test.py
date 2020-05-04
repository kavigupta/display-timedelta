import unittest
from datetime import timedelta

from display_timedelta import display_timedelta


class CheckVersionTest(unittest.TestCase):

    def testAllFour(self):
        self.assertEqual("4 days, 3 hours, 5 minutes, and 2 seconds",
                         display_timedelta(timedelta(days=4, hours=3, minutes=5, seconds=2)))
        self.assertEqual("1 day, 3 hours, 5 minutes, and 2 seconds",
                         display_timedelta(timedelta(days=1, hours=3, minutes=5, seconds=2)))
        self.assertEqual("1 day, 1 hour, 1 minute, and 1 second",
                         display_timedelta(timedelta(days=1, hours=1, minutes=1, seconds=1)))

    def test1Missing(self):
        self.assertEqual("1 hour, 1 minute, and 1 second",
                         display_timedelta(timedelta(hours=1, minutes=1, seconds=1)))
        self.assertEqual("1 day, 1 minute, and 1 second",
                         display_timedelta(timedelta(days=1, minutes=1, seconds=1)))
        self.assertEqual("1 day, 1 hour, and 1 second",
                         display_timedelta(timedelta(days=1, hours=1, seconds=1)))
        self.assertEqual("1 day, 1 hour, and 1 minute",
                         display_timedelta(timedelta(days=1, hours=1, minutes=1)))

    def test2Missing(self):
        self.assertEqual("7 hours and 1 second",
                         display_timedelta(timedelta(hours=7, seconds=1)))

    def testOnlyOne(self):
        self.assertEqual("7 hours",
                         display_timedelta(timedelta(hours=7)))

    def testRightNow(self):
        self.assertEqual("right now",
                         display_timedelta(timedelta(seconds=0)))

    def testRounding(self):
        self.assertEqual("5 minutes",
                         display_timedelta(timedelta(minutes=5, seconds=0.2)))
        self.assertEqual("right now",
                         display_timedelta(timedelta(seconds=0.2)))
        self.assertEqual("right now",
                         display_timedelta(timedelta(seconds=0.99999)))

    def testYears(self):
        self.assertEqual("2734032 days", display_timedelta(timedelta(days=2734032)))

    def testInPast(self):
        self.assertRaises(ValueError, lambda: display_timedelta(timedelta(seconds=-2)))
