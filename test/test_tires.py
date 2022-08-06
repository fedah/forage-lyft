from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoPrimeTires
from unittest import TestCase

class TestTires(TestCase):
    def test_carrigan_needs_service(self):
        tire_wears = [.5, .1, .4, .9]
        tires = CarriganTires(tire_wears)
        self.assertTrue(tires.needs_service())
    
    def test_carrigan_not_need_service(self):
        tire_wears = [.5, .1, .4, .7]
        tires = CarriganTires(tire_wears)
        self.assertFalse(tires.needs_service())

    def test_octoprime_needs_service(self):
        tire_wears = [.7, .7, .8, .8]
        tires = OctoPrimeTires(tire_wears)
        self.assertTrue(tires.needs_service())

    def test_octoprime_not_need_service(self):
        tire_wears = [.1, .1, .1, .1]
        tires = OctoPrimeTires(tire_wears)
        self.assertFalse(tires.needs_service())