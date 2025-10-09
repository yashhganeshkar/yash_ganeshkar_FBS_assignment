
# Write a program to print list after removing even numbers.

li = []

total = int(input("Enter the Number of elements You want to add in list = "))

for num in range(1,total+1):
    element = int(input(f"Enter Number {num} = "))
    li.append(element)

oddNumbers = []

for ele in li:
    if(ele%2 != 0):
        oddNumbers.append(ele)

print(oddNumbers)