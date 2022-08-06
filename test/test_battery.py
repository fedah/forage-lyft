from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from datetime import datetime, timedelta
from unittest import TestCase


class TestBattery(TestCase):
    def test_spindler_needs_service(self):
        current_date = datetime.now()
        #This model needs service every 3 years and 1125 days is over 3 years
        last_service_date = current_date - timedelta(days = 1125)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_spindler_not_need_service(self):
        current_date = datetime.now()
        #This model needs service every 3 years and 365 days is about 1 year
        last_service_date = current_date - timedelta(days = 365)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

    def test_nubbin_needs_service(self):
        current_date = datetime.now()
        #This model needs service every 4 years and 1500 days is over 4 years
        last_service_date = current_date - timedelta(days = 1500)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_not_need_service(self):
        current_date = datetime.now()
        #This model needs service every 4 years and 750 days is about 2 years
        last_service_date = current_date - timedelta(days = 750)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())