friends = [("Hina",27),
           ("Ayesha",25),
           ("Rabia",23),
           ("Alishba",21),
           ("Bushra",19),
           ("Laiba",17),
           ("Dia",15)]
age = lambda data:data[1] >=18
movie_buddies=list(filter(age,friends))
for i in movie_buddies:
    print(i)