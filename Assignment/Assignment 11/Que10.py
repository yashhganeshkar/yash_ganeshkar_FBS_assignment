
# Write a program to print list after removing even numbers.

li = [8,5,4,2,9,6,3,12,18,20]

updatedLists = []

for ele in li:
    if(ele%2 != 0):
        updatedLists.append(ele)

print(updatedLists)