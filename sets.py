#unordered,which means they cannot be accesseed by index oe key. they re also unchangeable

myset= {"apple", "banana", "cherry"}
for x in myset:
    print(x)

print ("banana" in myset)

#to add to a set, you can use .add
myset.add("kiwi")
print(myset)

#.update to add one list to another list
tropical= {"pineapple", "mango", "papaya"}
myset.update(tropical)
print(myset)