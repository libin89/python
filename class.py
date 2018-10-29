## import class from module
# for example, has a file: module_name.py, class: Car ElectricCar
# import module_name -> call classes via module_name.Car
# from module_name import Car -> call Car directly
# from module_name import Car, ElectricCar -> call both class directly
# from module_name import * -> call all classes directly, but not be recommended

# Create and use class
class Car():
    """anolog to make a car"""

    def __init__(self, make, model, year):
        """init car's property"""
        self.make = make
        self.model =  model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return car's completed description"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def fill_gas_tank(self):
        print("Car's gas tank is full.")
        
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.update_odometer(3)
my_new_car.read_odometer()


# inheritance
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
class ElectriCar(Car):
    """Electric car's special thing"""
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")
        
my_tesla = ElectriCar('tesla', 'model s', 2006)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
