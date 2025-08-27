'''fruits= ["apple", "banana", "cherry"]
for x in fruits:
    
    if x == "banana":
        continue
    print(x)
        
        
for x in "banana":
    print(x)


for x in range(0,6):
    print(x)

for x in range(2,30,3): #here it prints range 2-30 with increament of 3
    print(x)'''

for x in range(6):
    print (x)
else:
    print("finally finished")


adj= ["red", "big", "tasty"]
fruits= ["apple", "banana", "cherry"]

for x in adj:
    for y  in fruits:
        print(x,y)

#for loops cannot be left empty. if for one reason you for loop should be empty, use pass
for x in [0,1,2]:
    pass