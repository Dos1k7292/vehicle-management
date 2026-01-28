from car import Car
from motorcycle import Motorcycle
from garage import Garage
from fleet import Fleet

car = Car("Toyota", "Camry", 2020, 4, "Auto")
bike = Motorcycle("Yamaha", "R1", 2021, "Sport", False)

garage = Garage()
garage.add(car)
garage.add(bike)

fleet = Fleet()
fleet.add_garage(garage)

car.start_engine()
