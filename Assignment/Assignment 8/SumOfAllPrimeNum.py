
def SumOfPrimeNumber(num):
    addition = 0
    for i in range(2, num+1):
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            addition += i
    return addition

num = int(input("Enter Your Number = "))

print(SumOfPrimeNumber(num))
