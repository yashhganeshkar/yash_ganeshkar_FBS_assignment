
# Write a program to print all numbers which are divisible by m and n in the list.

li = []

total = int(input("Enter the Number of elements You want to add in list = "))

for num in range(1,total+1):
    element = int(input(f"Enter Number {num} = "))
    li.append(element)


m = int(input("Enter m = "))
n = int(input("Enter n = "))

for ele in li:
    if(ele%m == 0 and ele%n == 0):
        print(ele)

