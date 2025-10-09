
# Write a program to find maximum and minimum element in a list.

def minimum(li):
    minNo = li[0]

    for i in li:
        if(minNo > i):
            minNo = i
    
    return minNo


def maximum(li):
    maxNo = li[0]

    for i in li:
        if(maxNo < i):
            maxNo = i
    
    return maxNo


li = []

total = int(input("Enter the Number of elements You want to add in list = "))

for num in range(1,total+1):
    element = int(input(f"Enter Number {num} = "))
    li.append(element)

print(f"Minimum No of List is = {minimum(li)}")
print(f"Maximum No of List is = {maximum(li)}")
