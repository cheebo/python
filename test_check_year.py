from unittest import TestCase
from year import check_year

class Test(TestCase):
    def test_leap_year(self):
        self.assertEqual(check_year(2004), True)

    def test_dividable_by_400(self):
        self.assertEqual(check_year(2400), True)

    def test_dividable_by_100(self):
        self.assertEqual(check_year(2300), False)

    def test_dividable_by_4(self):
        self.assertEqual(check_year(4), True)
        self.assertEqual(check_year(32), True)
        self.assertEqual(check_year(2004), True)
