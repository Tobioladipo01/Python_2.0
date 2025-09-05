#polymorphism just shows that a method can have same name but different forms. here, move has different functions in different classes

class Boat:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model= model
    def move (self):
        print("Sail!")

class Plane:
    def __init__ (self, brand, model):
            self.brand= brand
            self.model= model
    def move(self):
            print("Fly!")

class Car:
    def __init__ (self, brand, model):
        self.brand= brand
        self.model= model
    def move(self):
        print ("Drive!")

Car1 = Car("Toyota", "Scienna")
Boat1 = Boat ("Ibiza", "Touring 20")
Plane1 = Plane ("Boeing", "747")

for x in (Car1, Boat1, Plane1):
     x.move()
#this for loop possible because of polymorphism
#for loop can also be written like this
vehicle = [Car1, Boat1, Plane1]
for x in vehicle:
     x.move()




class Vehicle:
     def __init__ (self, brand, model):
          self.brand = brand
          self.model = model
     def move(self):
        print("Move!")

class Car(Vehicle):
     pass

class Boat(Vehicle):
     def move(self):
          print ("Sail!")

class Plane(Vehicle):
     def move(self):
          print("Fly!")

c1= Car ("Toyota", "Camry")
b1= Boat ("Ibiza", "idk")
p1= Plane("Emirates", "C130")

print(c1.model)
for x in (c1, b1, p1):
     x.move()