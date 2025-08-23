thislist= ["apple", "pear", "pawpaw","mango", "banana"]
"""for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

[print (x) for x in thislist] ##list comprehension """


'''thislist= ["apple", "pear", "pawpaw","mango", "banana"]
newlist= []
for x in thislist:
    if "n" in thislist:
        newlist.append(x)
print (newlist)'''

# formula for list comprehension = expression FOR value IN iterable 

doubles=[]
for x in range(1,11):
    doubles.append(x*2)
print (doubles)


doubles = [x*2 for x in range(1,11)]
print (doubles)

triples= [x*3 for x in range(1,21)]
print (triples)

fruits= ["banana", "apple", "pawpaw", "mango"]
select= [x for x in fruits if "n" in x]
print (select)