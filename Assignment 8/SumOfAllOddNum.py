
def oddSum(num):
    addition = 0
    for i in range(1,num+1):
        if(i % 2 != 0):
            addition += i
    
    return addition

num = int(input("Enter Number = "))
print(oddSum(num))