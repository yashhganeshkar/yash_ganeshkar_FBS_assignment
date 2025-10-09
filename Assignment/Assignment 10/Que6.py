
# Write a program to remove duplicates from the list.

li = []

total = int(input("Enter the Number of elements You want to add in list = "))

for num in range(1,total+1):
    element = int(input(f"Enter Number {num} = "))
    li.append(element)

uniqueList = []

for ele in li:
    if(ele not in uniqueList):
        uniqueList.append(ele)

print(uniqueList)