#to create a class, use class. classes are like the folder or the group name while objects are the members
# in an object, you have two things two things. the attribute(variable) and the behaviour(functions)
# a class is bascially a blueprint from where you can make objects
# __init__ creates the objects for us



class Myclass:
    x=5

# to create an object named pl and print the vales of x
pl= Myclass()
print(pl.x)

class Cars:
    def __init__ (self, model, color, year, seats):
        self.model = model
        self.color = color
        self.year = year
        self.seats = seats

    def motion(self):
        print("car is moving averagely")
    def static(self):
        print("car engine is off")

car1=Cars("toyota", "black", 2025, 5)
print(car1.color)


class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

p1 = Person("Tobi", 23)
print (p1.name)

