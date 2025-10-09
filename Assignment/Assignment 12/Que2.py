
# Python Program to Remove the nth Index Character from a Non-Empty String

name = "Yashh Ganeshkar"

newName = ""

target = 7

for i in range(len(name)):
    if(target == i):
        continue
    newName += name[i]

print(newName)