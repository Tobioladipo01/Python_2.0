# used to perform search in regular expressions. you start by importing the re module( +, * and {} are quantifiers used to search for the number of occurances)
# \d will search for a single numerical digit.   \d\d two consequtive numerical digit   \s for space  \w for all digits and letter and _


import re
txt = "The raain in spain"
x= re.search("^The.raain$", txt)

print(x)

import re
names = ["Tobi Oladipo", "Murtala Mohammad", "Williams Kumuyi", "Goodluck Jonathan", "Elon Musk", "john"]
#find people with first and last name only
regex= "^\w+ \w+$"
for name in names:
    result= (re.search(regex, name))
    if result:
        print(name)


regex2= "^[a-zA-Z]+$"
for n in names:
    if re.search(regex2, n):
        print(n)
    

'''regex3 = "[a-zA-Z0-9]+@[a-zA-z]+\.(com|edu|net)"
userinput= input()
if re.search(regex3, userinput):
    print ("Valid email")
else:
    print("Input a valid email")'''

#.findall returns all your results in a list
#.split cuts out that particular thing youre looking for
quote = "There's only one thing i hate more than lying: Skin milk. which is water that's lying about being milk. -Ron Swanson"
pattern= "milk"
print (re.search(pattern, quote))
print (re.findall(pattern, quote))
print (re.split(pattern, quote))
print(re.sub("hate", "love", quote))






