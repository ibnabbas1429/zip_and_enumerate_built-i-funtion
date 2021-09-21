#creating the list
manifest = [("banana", 15),("mattresses",34),("dog kennels",42),("Machine", 120),("cheeses", 5)]

#Using the zip method
items, weights = zip(*manifest)

print(items)

print(weights)

"""items= ["banana", "matress", "dog kennel","machine", "cheeses"]

weights = [15, 34, 42, 120, 5]


print(list(zip(items, weights)))
cargo_item =[]

cargo_weight =[]
for item, weight in zip(items,  weights):
    
    cargo_item.append(item)
    
    cargo_weight.append(weight)
    #print(item, weight)
print(cargo_item)
print(cargo_weight)"""

items= ["banana", "matress", "dog kennel","machine", "cheeses"]
#for i, item in zip(range(len(items)), items):
    #print(i, item)
for item in items:
    print(zip(list(items)))

#using the enumerate method
for i, item in enumerate(items):
    print(i, item)




