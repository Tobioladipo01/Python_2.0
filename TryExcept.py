try:
    print(x)
except:
    print ("You might want to recheck your code again")

#with try except, if you have an invalid cose or errornous couse under try, instead of returning an error, it executes the except

# you can also specify what should be displayed for differnt types of error

try:
    print(y)
except NameError:
    print ("Variable y is not defined")
except:
    print("Something else went wrong")
#Here the supposed error is supposed to be a name error and instead of that, it executed our except block


#you use else to return a statment if no errors were raised
try:
    print("Hello")
except:
    print ("something went wrong")
else:
    print("Nothing went wrong")


#finally is exececuted if the block raises an error or not
try:
    print(a)
except:
    print("Something went wrong")
finally:
    print("try except code ended")


# you use the raise to define the error yourself
'''x=-1
if x<0:
    raise Exception("Sorry no numbers below zero")'''

c = "hello"
if c!= int:
    raise Exception("Input a number")