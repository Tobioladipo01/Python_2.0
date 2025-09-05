#when a variable is inside a function, it belongs only to that function and that is a local scope

def myfunc():
    x=100
    print (f"your value is {x}")
myfunc()

def anotherfunc():
    x=300
    def myinnerfunc():
        print (f"this is {x}")
    myinnerfunc()
anotherfunc()

#global scope
z=400
def globalfunc():
    print(z)
globalfunc()


# if you have two variables with thesame name and one is local and the other global, python treats them as two seperate variables
y=2
def frrfunc():
    y=80
    print (y)
frrfunc()
print (y)

#you can use the global keyword to make a local variable a global one
def anotherfunc():
    global a
    a=100
    print(a)
anotherfunc()
print (a) #print(a) wouldnt have worked if a wasnt a global variable

# you can also change the value of a global variable from inside a function
b=300
def bfunc():
    global b
    b=150
    print (b)
bfunc()

#for functions inside functions, we use the "nonlocal" keyword to make a local variable belong to the outer variable
def myfunc1():
    name = "Jane"
    def myfunc2():
        nonlocal name
        name = "Tobi"
    myfunc2()
    return name
print(myfunc1())

