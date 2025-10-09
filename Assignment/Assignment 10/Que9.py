
# Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

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

print(f"Even = {even}")
print(f"Odd = {odd}")
