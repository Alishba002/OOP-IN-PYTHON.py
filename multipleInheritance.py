class prey:
    def flee(self):
        print("this animal flee")
class predator:
    def hunt(self):
        print("this animal hunt")
class Rabbit(prey):
    pass
class Fish(prey,predator):
    pass
class Hawk(predator):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()