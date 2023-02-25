from abc import ABC , abstractmethod

class Vehical(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehical):
    def go(self):
        print("you drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehical):
    def go(self):
        print("You drive the Motorcycle")

    def stop(self):
        print("This motorcycle is stopped")

# vehical = Vehical()
car = Car()
motorcycle = Motorcycle()

# vehical.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()