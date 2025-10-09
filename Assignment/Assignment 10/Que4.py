
# Write a program to reverse the list.

li = []

total = int(input("Enter the Number of elements You want to add in list = "))

for num in range(1,total+1):
    element = int(input(f"Enter Number {num} = "))
    li.append(element)

revList = []

for ele in range(len(li)-1,-1,-1):
    revList.append(li[ele])

print(revList)