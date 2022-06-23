from .tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_sensors):
        self.tire_sensors = tire_sensors

    def needs_service(self) -> bool:
        # greater than or equal to 3 sum of all
        sum = 0
        for reading in self.tire_sensors:
            sum += reading
        
        return sum >= 3
        

