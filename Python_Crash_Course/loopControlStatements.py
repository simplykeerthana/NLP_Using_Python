# -*- coding: utf-8 -*-

# two types of loops in python 
# break statemetns 


for i in range(1,11):
    if i > 5:
        break
    print(i)
    
#continue 
print("\n")

for i in range(1, 11):
    if i>=4 and i<=7:
        continue
    print(i)
    
#pass, is like a null statement
    
i  = 1

if(i==1):
    pass
else:
    pass