# -*- coding: utf-8 -*-

#non homogeneous collection of elements 

list1 = [12, 12.8, "This is a string"]

print(list1)
print(list1[0])
print(list1[1])
print(list1[2])

#inserting elements 

list1.append(50)
list1.insert(0, "string number 1")

#updating list

print("updated list")

print(list1)
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])

#deleting list elements 

list1.pop()
print(list1)
del list1[2]
print(list1)

#length of the list 
print(len(list1))

for index in range(0, len(list1)):
    print(list1[index])
    
for index in range(0, len(list1)):
    list1[index] = 12
    
for item in list1:
    print(item)
    
print(list1)