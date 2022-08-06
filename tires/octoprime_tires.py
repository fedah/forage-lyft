from tires.tires import Tires

class OctoPrimeTires(Tires):
    def __init__(self, tire_wears):
        self.tire_wears = tire_wears
    
    def needs_service(self):
        if sum(self.tire_wears) >= 3:
            return True
        else:
            return False