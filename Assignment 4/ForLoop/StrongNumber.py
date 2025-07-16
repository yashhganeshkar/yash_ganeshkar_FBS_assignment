
num = int(input("Enter Number = "))

temp = num

Sum = 0

while(num != 0):

    a = num % 10
    num = num // 10

    fact = 1
    for i in range(1, a+1):
        fact *= i
    
    Sum = Sum + fact

if(temp != Sum):
    print("Not a Strong Number")
else:
    print("Strong Number")
