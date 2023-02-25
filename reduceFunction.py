import functools

# word = ["H","E","L","L","O"]
# func = functools.reduce(lambda x,y:x+y,word)
# print(func)

#               factorial

fact = [5,4,3,2,1]
result = functools.reduce(lambda x,y:x*y,fact)
print(result)