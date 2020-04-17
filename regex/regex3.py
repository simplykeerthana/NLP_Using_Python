# -*- coding: utf-8 -*-


import re

sentence = "I love Avengers Avengers"

print(re.sub(r"Avengers", "Justice League", sentence)) #replace the pattern 

print(re.sub(r"[a-z]", "0", sentence,1, flags=re.I)) # the count 1 is to match and replace that many character


