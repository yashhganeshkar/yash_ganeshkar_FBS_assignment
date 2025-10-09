
# WAP to print factorial of a number.

num = int(input("Enter a number = "))

fact = 1

start = 1

while(start <= num):
    fact *= start
    start += 1

print(fact)