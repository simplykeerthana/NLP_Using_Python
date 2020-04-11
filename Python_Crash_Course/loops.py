# -*- coding: utf-8 -*-

"""
while condition:
    statements
"""

i = 1

while i<10:
    print(i)
    i += 1
    
for i in range(1,11):
    print(i)
    
"""
12345
12345
12345
12345
using nested loops
"""

for i in range (1,6):
    for j in range(1,6):
        print(j, end = " ")
    print()