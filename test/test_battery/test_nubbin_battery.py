import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_is_true(self):
        current_date = date.fromisoformat("2021-06-15")
        last_service_date = date.fromisoformat("2016-10-15")

        battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)

        self.assertTrue(battery.needs_service())

    def test_needs_service_is_false(self):
        current_date = date.fromisoformat("2021-06-15")
        last_service_date = date.fromisoformat("2017-10-15")

        battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)

        self.assertFalse(battery.needs_service())
