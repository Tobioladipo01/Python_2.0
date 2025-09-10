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
    print (re.search(regex, names))



