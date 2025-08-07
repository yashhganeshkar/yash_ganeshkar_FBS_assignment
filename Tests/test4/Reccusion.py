

def Factorials(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    print(F"{num} = {fact}")
    if(num == 1):
        return fact
    Factorials(num-1)

num = int(input("Enter Your Number = "))

Factorials(num)