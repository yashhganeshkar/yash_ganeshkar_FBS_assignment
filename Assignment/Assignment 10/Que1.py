
# Write a program to find sum of all elements of list

li = []

total = int(input("Enter the Number of elements You want to add in list = "))

for num in range(1,total+1):
    element = int(input(f"Enter Number {num} = "))
    li.append(element)

addition = 0

for i in li:
    addition += i

print(f"Sum of Series = {addition}")