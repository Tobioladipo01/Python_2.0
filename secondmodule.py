import mymodule as mx

mx.greeting("tobi")

print(mx.person1["age"])


import platform
x= platform.system()
print(x)  #an inbuild module in python

# dir() another inbuilt module that lists all the variable names in a module
import mymodule
print(dir(mymodule))

#you can chooose to import inly parts from a module using the from keyword
from mymodule import person1
print (person1["age"])  #here you dont have to do print (module1.person["age"]) because you only imported person1
