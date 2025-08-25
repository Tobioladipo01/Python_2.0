thisdict = {
    "brand":"ford",
     "model": "mustang",
     "year": 2005,
     "colors": ["red", "blue", "green"]
}
print (thisdict)

x= thisdict["model"]
print (thisdict.keys())

thisdict["owner"]= "random"
print (thisdict)

#.values bring out a list of all the values on the dictionary while .keys brings out all the keys

#.pop removes an item
thisdict.pop("year")
print(thisdict)

for x in thisdict:
    print (x)

for x in thisdict:
    print(thisdict[x])

mydict= thisdict.copy()
print(mydict)
