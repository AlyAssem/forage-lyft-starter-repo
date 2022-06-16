import unittest

from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_is_true(self):
        current_milage = 100000
        last_service_milage = 30000

        engine = WilloughbyEngine(current_mileage=current_milage, last_service_mileage=last_service_milage)

        self.assertTrue(engine.needs_service())

    def test_needs_service_is_false(self):
        current_milage = 100000
        last_service_milage = 54000

        engine = WilloughbyEngine(current_mileage=current_milage, last_service_mileage=last_service_milage)

        self.assertFalse(engine.needs_service())
