## Dictionaries in python
car = {
    "Brand" : ["Ford","Masserati"],
    "model" : ["Mustang","Turismo"],
    "year" : [1964,2021]
    }

print(car)
x = car.keys() # returns a list with keys or dictionaries.


car["color"] = "white" # value by key
print(car.keys())
#print(x)
#print(car)
#print(car.values())
#print(car.items())

#car.pop("model")
#print(car)

#y = input("ENter the search element : ")
print(car["Brand"],"\n",type(car["Brand"]))
#b = if y in car["Brand"]
    
