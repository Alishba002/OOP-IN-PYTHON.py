class Car:

    def turn_on(self):

        print("you star the engine")
        return self

    def drive(self):

        print("you driva the car")
        return self
    def breaks(self):
        print("you step on breaks")
        return self

    def turn_off(self):
        print("you turn off the car")
        return self


car = Car()
# car.turn_on() this was the simple method
# car.drive()

# method chaining
# car.turn_on().drive()
# car.breaks().turn_off()
# can also:
car.turn_on()\
    .drive()\
    .breaks()\
    .turn_off()