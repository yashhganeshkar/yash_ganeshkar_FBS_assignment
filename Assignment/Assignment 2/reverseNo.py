
#Reverse Number

num = int(input("Enter 2 digit Number = "))

a = num // 10
b = num % 10

reverse = b * 10 + a

print(reverse)