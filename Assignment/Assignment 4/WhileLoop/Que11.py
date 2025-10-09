
# WAP to check if given number Strong Number.

num = int(input("Enter Your Number ="))

temp = num

addition = 0

while(num != 0):
    lastDigit = num % 10
    num = num // 10

    fact = 1
    for i in range(1,lastDigit+1):
        fact *= i
    
    addition += fact

if(addition == temp):
    print("Strong Number")
else:
    print("Not a Strong Number")