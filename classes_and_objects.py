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

    def intro (self):
        print (f"my name is {self.name}")

p1 = Person("Tobi", 23)
print (p1.name)
p1.intro()


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance= int(balance)
        self.age= 22
    
    def balance (self):
        print("your new balance is self.balance")
    def deposit (self, amount):
        balance = int(self.balance + amount)
        print (f"amount of {amount} have been deposited to your account. new balance is {balance}")
    def withdraw (self, amount):
        balance= int (self.balance-amount)
        print (f"amount of {amount} have been withdrawn from your account. new balance is {balance}")
    
Tobi = BankAccount ("Tobi", 1000000)
Tobi.deposit(500000)
print(Tobi.owner)

#to modify an object
Tobi.age = 23
print(Tobi.age)
# to delete, you use del Tobi.age
# to delete object, use del Tobi

#classes cannot be left empty if you class dont have a content, use pass
class Empty:
    pass
