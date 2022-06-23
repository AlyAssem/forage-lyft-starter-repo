import unittest

from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_is_true(self):
        tire_sensors = [0.8, 0.8, 0.8, 0.8]
        tire = OctoprimeTires(tire_sensors)

        self.assertTrue(tire.needs_service())

    def test_needs_service_is_false(self):
        tire_sensors = [0.6, 0.7, 0.4, 0.3]
        tire = OctoprimeTires(tire_sensors)

        # assertFalse passes even if the function doesn't return False.
        self.assertEqual(tire.needs_service(), False)
