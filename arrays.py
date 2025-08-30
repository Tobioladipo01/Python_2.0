# in python, lists work as arrays but you could always import arrays by importing the NumPy library

cars = ["ford", "volvo", "BMW"]
print(cars[1])
x = cars[2]
print (x)

# modify the vale of an array item
cars[0]= "Toyota"
print (cars)
print (len(cars))

for x in cars:
    print(x)

cars.append("Mercedes")
cars.append("Honda")
print (cars)
cars.remove("Honda")
print (cars)
cars.pop(1)
print(cars)