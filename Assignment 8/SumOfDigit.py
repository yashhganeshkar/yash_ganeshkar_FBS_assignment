
def SumOfDigit(num):

    addition = 0

    while(num != 0):
        l = num % 10
        num = num // 10
        addition += l
    
    return addition

num = int(input("Enter Number = "))

print(SumOfDigit(num))