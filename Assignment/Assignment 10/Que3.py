
# Write a program to find the second largest element in the list.

li = []

total = int(input("Enter the Number of elements You want to add in list = "))

for num in range(1,total+1):
    element = int(input(f"Enter Number {num} = "))
    li.append(element)

largest = li[0]
second_largest = None

for num in li:
    if(num > largest):
        second_largest = largest
        largest = num

print(second_largest)
