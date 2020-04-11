# -*- coding: utf-8 -*-

inp = input("Enter a number")
number1 = int(inp)

inp = input("enter a number")
number2 = int(inp)

print(number1 + number2)

#File I/O

#writing to a file

inp = input("Enter some text: ")

with open("textFiletxt", "w") as f:
    f.write(inp)
    
with open("textFile.txt", "a") as f:
    f.write(inp)

with open("textFile.txt", "r") as f:
    print(f.read())
    
