
# Write a program to create a duplicate of an existing list. It should not point to
# same list.

li = []

total = int(input("Enter the Number of elements You want to add in list = "))

for num in range(1,total+1):
    element = int(input(f"Enter Number {num} = "))
    li.append(element)

liCopy = []

for i in li:
    liCopy.append(i)

print(liCopy)