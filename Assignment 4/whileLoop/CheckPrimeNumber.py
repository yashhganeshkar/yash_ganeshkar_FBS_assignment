
num = int(input("Enter number = "))

i = 2

while(i < num):
    if(num % i == 0):
        print("Not a Prime Number")
        break
    i += 1
else:
    print("Prime Number")