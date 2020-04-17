# -*- coding: utf-8 -*-

import re

sentence1 = "Welcome to the year 2020"
sentence2 = "Just ~%* ++++---- arrived at @Jack's place.    #fun"
sentence3 = "I                love                u"

sentence1_modified  = re.sub(r'\d','', sentence1)

print(sentence1_modified) 

sentence2_modified = re.sub(r'[@#\.\']', '',sentence2)

print(sentence2_modified)

sentence2_modified = re.sub(r'\s+',' ',sentence2_modified)            
print(sentence2_modified)                   

sentence2_modified = re.sub(r"\s+[a-zA-Z]\s+",' ',sentence2_modified)
print(sentence2_modified)

sentence3_modified = re.sub(r'\s+',' ',sentence3)    

print(sentence3_modified)