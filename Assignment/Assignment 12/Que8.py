
# Python Program to Remove the Characters of Odd Index Values in a String

name = "Yashh Ganeshkar"

newName = ""

for i in range(len(name)):
    if(i%2 == 0):
        newName += name[i]

print(newName)