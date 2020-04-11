# -*- coding: utf-8 -*-

#introduction to python 

#key - Value Pairis 
dict1 = {}

dict1['apple'] = "Apple is a fruit"
dict1['orange'] = "Orange is a fruit"
dict1['car'] = "Carrs arer fast"
dict1['python'] = "I love python"

print(dict1)
print(dict1['apple'])
print(dict1['orange'])
print(dict1['apple'])

print(dict1.get("apple" ,"key doesnt exist"))

print(dict1.get("success" ,"key doesnt exist"))

del dict1['apple']

print(dict1)

print(len(dict1))


listOfKeys = list(dict1.keys())
listOfValues = list(dict1.values())

print("\n")
for key in dict1.keys():
    print(dict1[key])
    
for value in dict1.values():
    print(value)



