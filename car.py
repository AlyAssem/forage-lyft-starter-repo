from serviceable import Serviceable
from battery.battery import Battery
from engine.engine import Engine
from tires.tires import Tires
class Car(Serviceable):
    def __init__(self, engine: Engine, battery:Battery, tires: Tires):
        self.__engine = engine
        self.__battery = battery
        self.__tires = tires

    def needs_service(self):
        return self.__engine.needs_service() or self.__battery.needs_service() or self.__tires.needs_service()

