from datetime import date
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        capulet_engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        spindler_battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)

        car = Car(battery=spindler_battery, engine=capulet_engine)
        
        return car

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        Willoughby_engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        spindler_battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)

        car = Car(battery=spindler_battery, engine=Willoughby_engine)
        
        return car

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_is_on: bool) -> Car:
        sternman_engine = SternmanEngine(warning_light_is_on=warning_light_is_on)
        spindler_battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)

        car = Car(battery=spindler_battery, engine=sternman_engine)
        
        return car

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        willoughby_engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        nubbin_battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)

        car = Car(battery=nubbin_battery, engine=willoughby_engine)
        
        return car

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        capulet_engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        nubbin_battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)

        car = Car(battery=nubbin_battery, engine=capulet_engine)
        
        return car

        


# today = datetime.today().date()
# last_service_date = today.replace(year=today.year - 5)
# current_mileage = 0
# last_service_mileage = 0

# capulet_engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
# spindler_battery = SpindlerBattery(current_date=today, last_service_date=last_service_date)

# car = Car(battery=spindler_battery, engine=capulet_engine)

# print(car.needs_service())