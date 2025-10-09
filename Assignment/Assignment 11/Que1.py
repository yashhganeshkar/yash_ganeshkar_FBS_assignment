
# Python Program to Put Even and Odd elements of a List into two Different Lists

li = []

total = int(input("Enter the Number of elements You want to add in list = "))

for num in range(1,total+1):
    element = int(input(f"Enter Number {num} = "))
    li.append(element)

even = []
odd = []

for ele in li:
    if(ele%2==0):
        even.append(ele)
    else:
        odd.append(ele)

print(even)
print(odd)