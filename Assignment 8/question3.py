
# Que.1) 1+ 2 + 3 + 4+..... + n

num = int(input("Enter Number = "))

addition = 0

for i in range(1, num+1):
    addition += i

print(addition)

# Que.2) 1!+ 2! + 3! + 4!+..... + n!

num = int(input("Enter number = "))

addition = 0

for i in range(1, num+1):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    addition += fact

print(addition)

# Que.3) 1^1 + 2^2 + 3^3+ ...... n^n

num = int(input("Enter Number = "))

addition = 0

for i in range(1, num+1):
    addition += (i**i)

print(addition)