
num = int(input("Enter Your Name = "))

for i in range(1, num+1):
    for j in range(1, num-i+1):
        print(" ", end=" ")
    
    for k in range(1, i+1):
        print(" * ", end=" ")
    
    print()