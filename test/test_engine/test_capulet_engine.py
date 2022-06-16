import unittest

from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_is_true(self):
        current_milage = 50000
        last_service_milage = 19999

        engine = CapuletEngine(last_service_mileage=last_service_milage, current_mileage=current_milage)

        self.assertTrue(engine.needs_service())

    def test_needs_service_is_false(self):
        current_milage = 50000
        last_service_milage = 25000

        engine = CapuletEngine(last_service_mileage=last_service_milage, current_mileage=current_milage)

        self.assertFalse(engine.needs_service())
