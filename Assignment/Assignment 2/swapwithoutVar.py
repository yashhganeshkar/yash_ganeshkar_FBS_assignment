
num1 = int(input("Enter No1 = "))
num2 = int(input("Enter No2 = "))

print("Num1 =",num1)
print("Num2 =",num2)

print("# First Approch")
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("Num1 =",num1)
print("Num2 =",num2)


# print("# Second Approch")
# num1 = num1 * num2
# num2 = num1 / num2
# num1 = num1 / num2

# print("Num1 =",num1)
# print("Num2 =",num2)

print("# Third Approch")
num1, num2 = num2, num1


print("Num1 =",num1)
print("Num2 =",num2)
