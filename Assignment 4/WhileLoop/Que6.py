
# WAP to check if a given number is prime number or not.

num = int(input("Enter Your Number = "))

start = 2

while(start < num):
    if(num % start == 0):
        print("Not Prime")
        break

    start += 1
else:
    print("Prime Number")