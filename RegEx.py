# used to perform search in regular expressions. you start by importing the re module

import re
txt = "The raain in spain"
x= re.search("^The.raain$", txt)

print(x)

