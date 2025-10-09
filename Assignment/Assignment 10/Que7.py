
# Write a program to create a new list from existing list which contains cube of
# each number of list.

li = []

total = int(input("Enter the Number of elements You want to add in list = "))

for num in range(1,total+1):
    element = int(input(f"Enter Number {num} = "))
    li.append(element)

cubeList = []

for ele in li:
    cube = ele**3
    cubeList.append(cube)

print(cubeList)
