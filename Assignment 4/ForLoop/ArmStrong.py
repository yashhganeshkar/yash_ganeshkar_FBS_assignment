
num = int(input("Enter Number = "))

temp = num

addition = 0

numCount = 0

while(num != 0):
    a = num % 10
    num = num // 10
    numCount +=1

num = temp

while(num != 0):
    a = num % 10
    num = num // 10

    addition += (a**numCount)

if(temp == addition):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")