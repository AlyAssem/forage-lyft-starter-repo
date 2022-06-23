from .tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_sensors):
        self.tire_sensors = tire_sensors

    def needs_service(self) -> bool:
        for reading in self.tire_sensors:
            if reading >= 0.9:
                return True
            return False

