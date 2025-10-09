
# Python Program to Sum All the Items in a Dictionary

di = {
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5
}

addition = 0

for i in di:
    addition += di[i]

print(addition)