
# Write a program to create three lists of numbers, their squares and cubes

li = []

total = int(input("Enter the Number of elements You want to add in list = "))

for num in range(1,total+1):
    element = int(input(f"Enter Number {num} = "))
    li.append(element)

squares = []
cubes = []

for ele in li:
    squares.append(ele**2)
    cubes.append(ele**3)

print(li)
print("Squares = ",squares)
print("Cubes = ",cubes)
