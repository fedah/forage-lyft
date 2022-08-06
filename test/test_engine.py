from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from unittest import TestCase

class TestEngine(TestCase):
    def test_capulet_needs_service(self):
        current_mileage = 30001
        last_service_mileage = 0
        #This model needs service every 30,000 miles
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
    
    def test_capulet_not_need_service(self):
        current_mileage = 29999
        last_service_mileage = 0
        #This model needs service every 30,000 miles
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_willoughby_needs_service(self):
        current_mileage = 60001
        last_service_mileage = 0
        #This model needs service every 60,000 miles
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
    
    def test_willoughby_not_need_service(self):
        current_mileage = 59999
        last_service_mileage = 0
        #This model needs service every 60,000 miles
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_sternman_needs_service(self):
        warning_light_is_on = True
        #This model needs service only if the warning light is on 
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_sternman_not_need_service(self):
        warning_light_is_on = False
        #This model needs service only if the warning light is on 
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())
