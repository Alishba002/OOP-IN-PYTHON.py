class Cat:
    name = ""
    color = ""
    age = 0
    def __init__(ref,n,c,a):
        ref.name = n
        ref.color = c
        ref.age = a
        def run(self):
            print(self.name," is running")
        def sleep(self):
            print(self.name," is sleeping")
cat1 = Cat("jack","orange",5)
cat2 = Cat("oggy","purple",4)
print("cat1: ")
print(cat1.name,cat1.color,cat1.age)
cat1.run()
print("cat2: ")
print(cat2.name,cat2.color,cat2.age)
cat1.sleep()
