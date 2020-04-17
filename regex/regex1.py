# -*- coding: utf-8 -*-
 
#importing librarires

import re

sentence = "I was born iin yeear 1996"
sentence1= "abb"
print(sentence)

print(re.match(r".*", sentence)) #zero or more
print(re.match(r".+", sentence))#one of mroe
print(re.match(r"[a-zA-Z]+", sentence)) # looks for capital letters
print(re.match(r"ab?", sentence1)) #a or zero or 1 b