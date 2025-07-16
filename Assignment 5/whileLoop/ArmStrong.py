
num = int(input("Enter Number = "))

temp = num

count = 0

addition = 0

while(num != 0):
    a = num % 10
    num = num // 10
    count += 1

num = temp

while(num != 0):
    a = num % 10
    num = num // 10

    addition += (a ** count)

if(temp == addition):
    print("Arm Strong Number")
else:
    print("Not a Arm Strong Number")