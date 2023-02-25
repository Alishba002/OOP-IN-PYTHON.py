# def double(x):
#     return x*2
# print(double(5))

double = lambda x:x*2
multiply = lambda x,y:x*y
add =lambda x,y,z:x+y+z
full_name = lambda first_name,last_name:first_name+" "+last_name
print(full_name("Alishba","Abbas"))
age_check = lambda age:True if age >= 18 else False
print(age_check(21))
print(add(3,5,8))
print(multiply(6,7))
print(double(5))