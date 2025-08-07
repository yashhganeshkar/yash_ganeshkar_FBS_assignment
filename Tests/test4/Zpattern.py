
num = int(input("Enter Number = "))

for i in range(1, num+1):
    for j in range(1, num+1):
        if(i == 1 or i == num or (j == num-i+1)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    
    print()