
num = int(input("Enter Your Number = "))

i = 0

prev1 = 0
prev2 = 1
c = 0

while(i <= num):
    if(i >= 2):
        c = prev1 + prev2
        prev1 = prev2
        prev2 = c
        print(c)
    elif(i == 0):
        print(prev1)
    elif(i == 1):
        print(prev2)

    i += 1