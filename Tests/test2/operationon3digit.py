
# Opeartion on 3 digit number

num = int(input("Enter Your Number = "))

digit3 = num % 10

num = num // 10

digit2 = num % 10

num = num // 10

digit1 = num % 10

if(((digit2*2) == digit1) and ((digit3 / 2) == digit1)):
    print("Yes, You Have Done It!")
else:
    print("Please Try next Time!")
