
num = int(input("Enter Your Number = "))

if(num > 1):
    for i in range(2,num):
        if(num % i == 0):
            print("Not an Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Enter a Positive Number or Greater than 1")