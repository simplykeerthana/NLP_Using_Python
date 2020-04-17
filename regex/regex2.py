# -*- coding: utf-8 -*-

import re

sentence ="1996 was born in the I year born"

print(re.match(r"[a-zA-Z]+",sentence)) # IT ONLY SEARCHES The fiirst element iin teh sentence
print(re.search(r"[a-zA-Z]+",sentence))


#starts with 

if re.match(r"1996", sentence):
    print("match")
else:
    print("unmatch")


#ends with 
    
if re.search(r"born$", sentence): #dollar symbol is end of sentence
    print("match")
else:
    print("unmatch")