thislist= ["apple", "pear", "pawpaw","mango", "banana"]
'''thislist.sort()
print(thislist)

#to sort descending
thislist.sort(reverse=True)
print(thislist)

#normally, sorting gives prference to uppercase which may affect your list order. to ignore the case we use
thislist.sort(key=str.lower)

#to reverse the order
thislist.reverse()'''

newlist= thislist.copy()
print (newlist)

#list addition mathods
list1= ["a", "b", "c", "d"]
list2= [1,2,3,4]
list3= list1 + list2
print(list3)

for x in list1:
    list2.append(x)
print(list2)

