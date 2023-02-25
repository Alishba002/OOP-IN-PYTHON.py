store = [("pants",25000),
         ("shirt",34000),
         ("skirt",18000)]
# to_euro = lambda data:(data[0],data[1]*0.82)
# store_euro = list(map(to_euro,store))
to_dollars = lambda data:(data[0],data[1]/0.82)
store_dollars = list(map(to_dollars,store))
for i in store_dollars:
    print(i)
