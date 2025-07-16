
num = int(input("Enter Number = "))

addition = 0

for i in range(1,num):
    if(num % i == 0):
        addition += i

if(num == addition):
    print("Perfect Number")
else:
    print("Not an Perfect Number")