#executes a set of statements as long as the condition is true
i=1
while i<6:
    print(i)
    if i == 3:
        break
    i+=1
else:
    print("number too high")


age= int(input("Enter your age:"))
while age<0:
    print ("age cannot be negative")
    age= int(input("Enter your age:"))
print (f"you are {age} years old")


