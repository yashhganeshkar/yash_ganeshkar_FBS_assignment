
# Python Program to Replace all Occurrences of ‘a’ with $ in a String

name = "Yashh Ganeshkar"

newName = ""

for i in name:
    if(i == "a"):
        newName += "$"
        continue
    newName += i

print(newName)