class Animal:
    def eat(self):
        print("This animal is eating")
class Rabbit(Animal):
    def eat(self):
        print("This animal is sleeping")

rabbit = Rabbit()
rabbit.eat()
