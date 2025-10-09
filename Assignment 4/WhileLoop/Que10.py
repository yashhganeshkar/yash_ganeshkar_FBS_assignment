
# WAP to check if given number is Perfect Number.

num = int(input("Enter Your Number = "))

addition = 0

start = 1

while(start < num):
    if(num%start == 0):
        addition += start
    start += 1

if(addition == num):
    print("Perfect Number")
else:
    print("Not a Perfect Number")