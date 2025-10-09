
# WAP to check if given number is Perfect Number.

num = int(input("Enter Your Number = "))

addition = 0

for i in range(1,num):
    if(num%i==0):
        addition += i

if(addition == num):
    print("Perfect Number")
else:
    print("Not a Perfect Number")