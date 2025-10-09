
# WAP to check if a given number is prime number or not.

num = int(input("Enter Your Number = "))

for i in range(2,num):
    if(num % i == 0):
        print("Not Prime")
        break
else:
    print("Prime Number")