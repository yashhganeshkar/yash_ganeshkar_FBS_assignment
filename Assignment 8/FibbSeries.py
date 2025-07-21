
def FibbSeries(num):
    prev1 = 0
    prev2 = 1
    current = 0

    for i in range(1, num+1):
        if(i > 2):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current

            print(current)
        elif(i == 1):
            print(prev1)
        elif(i==2):
            print(prev2)


num = int(input("Enter Number = "))

FibbSeries(num)