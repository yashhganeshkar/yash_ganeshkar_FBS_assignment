
num = int(input("Enter Number = "))

temp = num

addition= 0

while(num != 0):
    a = num % 10
    num = num // 10

    fact = 1
    for i in range(1, a+1):
        fact *= i
    addition += fact

if(addition == temp):
    print("It is a strong Number")
else:
    print("It is not a strong Number")
