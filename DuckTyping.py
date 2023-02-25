class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is quacking")

class Chicken:
    def talk(self):
        print("This chicken is walking")
    def walk(self):
        print("This chicken is clunking")

class Person():
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You catch the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)