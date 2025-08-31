class Person:
    def __init__ (self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname (self):
        print (f"my name is {self.firstname} {self.lastname}")

p1 = Person ("Tobi", "Oladipo")
print (p1.firstname)
p1.printname()

#when you add an init function to a child class, that init function overrides the init of the parent class
class Student (Person):
    def __init__ (self, firstname, lastname):
        Person.__init__ (self, firstname, lastname) #this lines makes it inherit the parent's function

p2= Student ("Debo", "Oladipo")
print (p2.firstname)
p2.printname()


class Student (Person):
    def __init__ (self, firstname, lastname, graduationyear):
        super().__init__ (self, firstname, lastname) #super makes it inherit all the method and class from parent
        self.graduationyear=graduationyear
        #more variables can still be added to the child class


    #if theres nothing more to add to the child class, use pass. e.g
    class Teachers (Person):
        pass
    