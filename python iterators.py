nums = [1,2,4,5,6,8]
#for x in nums:
#    print (x)

it = iter (nums)
print(it.__next__())
print(it.__next__())
print(it.__next__())
#or
print(next(it))


mytuple = ("apple", "banana", "cherry")
it_tuple = iter (mytuple)

print(next(it_tuple))

mystr= "banana"
myiter= iter (mystr)
print(next(myiter))


#for loop is basically like a summarry for the whole iterators.
# creating an iterator, we use __iter__ instead of __init__ inside the class
# you cannot use the for loop to loop over the numbers of an integer. if you want to do that, you 
#need to create you own iterator

class Mynumbers:
    def __iter__ (self):
