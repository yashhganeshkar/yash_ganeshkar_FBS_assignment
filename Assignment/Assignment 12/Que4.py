
# Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged

name = "Yashh Ganeshkar"

fchar = name[0]
lchar = name[-1]

newName = lchar

for i in range(1,len(name)):
    newName += name[i]

newName += fchar

print(newName)