
# Python Program to replace every blank space with hyphen in a string.

name = "Yashh Rajkumar Ganeshkar"

newName = ""

for i in name:
    if(i == " "):
        newName += "-"
        continue
    newName += i

print(newName)