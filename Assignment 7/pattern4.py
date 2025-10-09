
num = int(input("Enter Number = "))

for i in range(1, num+1):
    for j in range(num-i):
        print(" ", end=" ")
    for k in range(1, i+1):
        print(k, end=" ")
    for a in range(1,i):
        print(a, end=" ")
        a -= 1
    print()