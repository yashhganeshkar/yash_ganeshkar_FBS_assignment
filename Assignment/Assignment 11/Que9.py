
# Write a program to create three lists of numbers, their squares and cubes

li = [2,3,4,5,6,7,8]

squares = []
cubes = []

for ele in li:
    squares.append(ele**2)
    cubes.append(ele**3)

print("Squares = ",squares)
print("Cubes = ", cubes)