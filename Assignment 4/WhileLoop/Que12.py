
# WAP to print Armstrong number within a given range

num = int(input("Enter Your Number ="))

temp = num

count = 0

addition = 0

while(num != 0):
    num = num // 10
    count += 1

num = temp

while(num != 0):
    lastDigit = num % 10
    num = num // 10

    addition += (lastDigit**count)

if(addition == temp):
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")