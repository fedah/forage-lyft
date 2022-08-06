import datetime
from battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.time_bewteen_service = 2
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + self.time_bewteen_service)
        
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False

        
