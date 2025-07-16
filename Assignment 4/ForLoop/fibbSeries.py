
num = int(input("Enter number = "))

prev1 = 0
prev2 = 1

for i in range(num+1):
    if(i >= 2):
        Next = prev1 + prev2
        prev1 = prev2
        prev2 = Next
        print(Next)
    elif(i == 0):
        print(prev1)
    elif(i == 1):
        print(prev2)