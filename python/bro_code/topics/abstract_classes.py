# Prevents a user from creating an object of that class 
# compels a user to override abstract methods in a child class 
# abstract class = a class which contains one or more abstract methods. 
# abstract method = a method that has a declaration but does not have an implementation. 

# To use abstract method and class we have to import the following
from abc import ABC, abstractmethod 

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")
    
    # def stop(self):
    #     print("You stop a car")


class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    # def stop(self):
    #     print("You stop the motorcycle")


car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()

# to not get error we need stop() in Car and Motorcycle class 

