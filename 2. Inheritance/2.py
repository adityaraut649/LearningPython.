# type of inheritance

# 1. Single Inheritance
#One child class inherits from one parent class

# Base class
class Vehicle:
    def start(self):
        print("Vehicle is starting")

# Child class
class Car(Vehicle):
    def honk(self):
        print("The car is honking")

# Object
car1 = Car()
car1.start()
car1.honk()

# 2. Multiple Inheritance
#Two child classes inherit from two parent classes

#Base Electric:
# Parent class 1
class Electric:
    def charge(self):
        print("The vehicle is charging")

# Parent class 2
class Engine:
    def fuel(self):
        print("The engine is using fuel")

# Child class
class HybridCar(Electric, Engine):
    def drive(self):
        print("The hybrid car is driving")

# Object
hybrid = HybridCar()
hybrid.drive()
hybrid.fuel()
hybrid.charge()


# 3. Hierarchical Inheritance
# A child class inherits from a parent class and the parent class inherits from another parent class
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def honk(self):
        print("Car is honking")

class Bike(Vehicle):
    def kick_start(self):
        print("Bike is starting with kick")

# Objects
c = Car()
b = Bike()

c.start()
c.honk()

b.start()
b.kick_start()

# 4. Multilevel Inheritance
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def honk(self):
        print("The car is honking")

class ElectricCar(Car):
    def charge(self):
        print("The car is charging")

# Object
e_car = ElectricCar()
e_car.start()
e_car.honk()
e_car.charge()

# HybridCar Inherits

class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def honk(self):
        print("Car is honking")

class Electric(Vehicle):
    def charge(self):
        print("Vehicle is charging")

class HybridCar(Car, Electric):
    def drive(self):
        print("Hybrid car is driving")

# Object
h = HybridCar()
h.start()
h.honk()
h.charge()
h.drive()