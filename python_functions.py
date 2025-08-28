#a function is a set of codes that only runs when it is calledd
'''def my_function():
    print("hello from a function")
my_function()


def happy_birthday(name, age):
    print(f"happy birthday to you {name}")
    print (f"you are {age} years old")
happy_birthday("Debo", 20)
#(name) here is like a temporary variable


def display_invoice(username, amount, due_date):
    print(f"hello {username}")
    print(f"your bill of {amount:.2f} is due on {due_date}")
display_invoice("Union", 1000, "Friday")


def add(first, second):
    c= int(first + second)
    print (f"the sume of {first} and {second} is {c}")
add(57, 45)


#add * behind the parameter name if you dont know how many arguments would be passed 
def my_function2(*kids):
    print(f"the youngest child is {kids[1]}")
my_function2("amina", "taiwo", "zarah")'''



def my_function3(food):
    for x in food:
        print(x)

fruits= ["apple", "banana", "cherry"]
my_function3(fruits)

def myfunction (x):
    return 5 * x
print(myfunction (5))

#  / to show a function only has positional argument
def another(x, /):
    print(x)
another(3)

#without the / you can use both positional and keyword arguments
def more (x):
    print(x)
more (x=7)

# *, makes sure the function only has keyword argument
def keyword(*, x):
    print (x)
keyword(x=5)

#you can combine postional and keyword. any variable before the ,/ is positional and any after ,* is keyword
def practice(a,b,/,*,c,d):
    print (a+b+c+d)
practice (3,4,c=5,d=6)


#recursion. you call the function inside the function block before calling outside
def walk(steps):
    if steps == 0:
        return
    walk(steps -1)
    print (f"i have taken {steps} number of steps")
walk(50)

#using for loop
def walks(steps):
    for x in range (1, steps + 1):
        print (f"i have taken {x} steps")
walks(50)