
num = int(input("Enter Your Number = "))

i = 1

addition = 0

while(i < num):
    if(num % i == 0):
        addition += i
    
    i += 1

if(num == addition):
    print("Perfect number")
else:
    print("Not a Perfect Number")