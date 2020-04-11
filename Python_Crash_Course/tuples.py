# -*- coding: utf-8 -*-

#same are lists but immutable

tuple1 = (12,"THis is a simple string", 13.8, "Another String")
tuple2 = (50,90,2)

print(tuple1)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

tuple3 = tuple1 + tuple2

print(len(tuple3))

for i in range(0, len(tuple3)):
    print(tuple3[i])


for item in tuple3:
    print(item)
    
#tuple is immutable, it cannot be updaated
