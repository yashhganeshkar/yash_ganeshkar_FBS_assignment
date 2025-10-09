
# WAP to print Fibonacci series upto n.

end = int(input("Enter Your End = "))

prev1 = 0
prev2 = 1

for i in range(1,end+1):
    if(i > 2):
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current
        print(current)
    elif(i == 1):
        print(prev1)
    elif(i == 2):
        print(prev2)