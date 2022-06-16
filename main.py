from datetime import datetime

from car_factory import CarFactory

def main():
    today = datetime.today().date()
    last_service_date = today.replace(year=today.year - 2)
    current_mileage = 0
    last_service_mileage = 0

    c1 = CarFactory.create_thovex(current_date=today, last_service_date=last_service_date
    , current_mileage=current_mileage, last_service_mileage=last_service_mileage)

    c2 = CarFactory.create_glissade(current_date=today, last_service_date=last_service_date,
     current_mileage=current_mileage, last_service_mileage=last_service_mileage)

    print(c1.needs_service())
    print(c2.needs_service())

if __name__ == '__main__':
    main()