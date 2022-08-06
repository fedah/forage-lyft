from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_wears):
        self.tire_wears = tire_wears
    
    def needs_service(self):
        for wear in self.tire_wears:
            if wear >= 0.9:
                return True
        return False