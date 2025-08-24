thislist= ["apple", "pear", "pawpaw","mango", "banana"]
thislist.sort()
print(thislist)

#to sort descending
thislist.sort(reverse=True)
print(thislist)

#normally, sorting gives prference to uppercase which may affect your list order. to ignore the case we use
thislist.sort(key=str.lower)

#to reverse the order
thislist.reverse()

