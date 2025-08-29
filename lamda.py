def add(x,y):
    return x+y
print (add(4,6))

add2=lambda x,y: x+y
# this means first line of you lambda function summarizes the first two lines of your normal function
print(add2(4,7))

print((lambda x,y: x+y)(4,5))

x= lambda a: a+10
print (x(5))

x = lambda a,b: a*b
print(x(5,6))

