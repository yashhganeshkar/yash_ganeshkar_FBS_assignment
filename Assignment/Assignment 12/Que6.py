
# Python Program to Take in a String and Replace Every Blank Space with Hyphen

name = "Yashh Rajkumar Ganeshkar"

newName = ""

for i in name:
    if(i == " "):
        newName += "_"
        continue
    newName += i

print(newName)