from datetime import datetime

from car_factory import CarFactory

def main():
    today = datetime.today().date()
    last_service_date = today.replace(year=today.year - 3)
    current_mileage = 0
    last_service_mileage = 0
    warning_light_is_on = False

    c1 = CarFactory.create_thovex(current_date=today, last_service_date=last_service_date
    , current_mileage=current_mileage, last_service_mileage=last_service_mileage)

    c2 = CarFactory.create_palindrome(current_date=today, last_service_date=last_service_date,
        warning_light_is_on=warning_light_is_on)

    print(c1.needs_service())
    print(c2.needs_service())

if __name__ == '__main__':
    main()