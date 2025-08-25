this_tuple= ("apple", "banana", "cherry", "grapes", "mango")

#items in a tuple cannot ne changed, redorderd, added to or removed from
print(len(this_tuple))

print(this_tuple[1])

if "banana" in this_tuple:
    print ("yes")

y= list(this_tuple)
print (y)

y.append("orange")
print(y)

this_tuple= tuple(y)
print(y)

#to add a tuple to another tuple, use +=
addtuple= ("beans", "rice", "spag")
this_tuple += addtuple
print (this_tuple)

#unpacking in python allows you take back the values of each tuple nack into individual variables
(protein, carbs, sweet)= addtuple
print (protein)
print (carbs)

#if the number of variables>no of values, use *to the last variable and the remaing values will be added to it as a list
(green, red, *blue) = this_tuple
print (green)
print (red)
print (blue)

for x in this_tuple:
    print(x)

for i in range(len(this_tuple)):
    print(this_tuple[i])

tuple1= ("name", "age", "sex")
tuple2= (1,2,3)
tuple3= tuple1 + tuple2
print (tuple3)

tuple4= tuple3 * 2
print(tuple4)

print("name" in tuple4)


