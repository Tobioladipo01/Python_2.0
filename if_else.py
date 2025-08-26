
a= 23
b= 23
if b>a:
    print ("b is greater than a")
elif b==a:
    print("b is equal to a")
else:
    print ("b is less than a")

print ("a is greater than b") if a>b else print ("a is equal to b")

#whenever print comes after if, you use : else you dont when doing the summarization

a=200
b=33
c=500
if a>b and c>a:
    print("both conditions are true")

if a>c or a>b:
    print("one of the conditions are true")

if not a>b:
    print ("a is not greater than b")

x= 41
if x>10:
    print ("above 10")
    if x>20:
        print ("and also above 20")
    else:
        print("but not above 20")
#nested if

#if you have an empty if statement, use pass. cos if cannot be empty
a=33
b=200

if b>a:
    pass
