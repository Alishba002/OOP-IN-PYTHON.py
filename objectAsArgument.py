class Car:
    color = None

class Motorcycle:
    color = None

def change_color(car,color):
    car.color = color

car1 = Car()
car2 = Car()
car3 = Car()

motor1 = Motorcycle()
motor2 = Motorcycle()
motor3 = Motorcycle()

change_color(car1,"red")
change_color(car2,"black")
change_color(car3,"blue")

change_color(motor1,"red")
change_color(motor2,"black")
change_color(motor3,"blue")

print(car1.color)
print(car2.color)
print(car3.color)

print(motor1.color)
print(motor2.color)
print(motor3.color)