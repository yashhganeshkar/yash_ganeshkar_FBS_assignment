
# Write a program to remove all occurrences of a given element in the list.

li = []

total = int(input("Enter the Number of elements You want to add in list = "))

for num in range(1,total+1):
    element = int(input(f"Enter Number {num} = "))
    li.append(element)

target = int(input("Enter Your Target = "))

for ele in li:
    if(target == ele):
        li.remove(ele)

print(li)