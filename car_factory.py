from datetime import date
from typing import List
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_sensors: List[float]) -> Car:
        capulet_engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        spindler_battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        carrigan_tires = CarriganTires(tire_sensors=tire_sensors)
        car = Car(battery=spindler_battery, engine=capulet_engine, tires=carrigan_tires)
        
        return car

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_sensors: List[float]) -> Car:
        Willoughby_engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        spindler_battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        carrigan_tires = CarriganTires(tire_sensors=tire_sensors)
        car = Car(battery=spindler_battery, engine=Willoughby_engine, tires=carrigan_tires)
        
        return car

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_is_on: bool, tire_sensors: List[float]) -> Car:
        sternman_engine = SternmanEngine(warning_light_is_on=warning_light_is_on)
        spindler_battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        octoprime_tires = OctoprimeTires(tire_sensors=tire_sensors)
        car = Car(battery=spindler_battery, engine=sternman_engine, tires=octoprime_tires)
        
        return car

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_sensors: List[float]) -> Car:
        willoughby_engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        nubbin_battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        octoprime_tires = OctoprimeTires(tire_sensors=tire_sensors)
        car = Car(battery=nubbin_battery, engine=willoughby_engine, tires=octoprime_tires)
        
        return car

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_sensors: List[float]) -> Car:
        capulet_engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        nubbin_battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        octoprime_tires = OctoprimeTires(tire_sensors=tire_sensors)
        car = Car(battery=nubbin_battery, engine=capulet_engine, tires=octoprime_tires)
        
        return car


# today = date.today()
# last_service_date = today.replace(year=today.year - 2)
# current_mileage = 0
# last_service_mileage = 0

# car = CarFactory.create_calliope(current_date=today, last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage, tire_sensors=[0.9, 0.3, 0.5, 0.3])

# print(car.needs_service())