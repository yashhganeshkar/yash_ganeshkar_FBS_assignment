

# WAP to print Fibonacci series upto n.

end = int(input("Enter Your End = "))

prev1 = 0
prev2 = 1

start = 1

while(start <= end):
    if(start > 2):
        current = prev1+prev2
        prev1 = prev2
        prev2 = current
        print(current)
    elif(start == 1):
        print(prev1)
    elif(start == 2):
        print(prev2)
    start += 1