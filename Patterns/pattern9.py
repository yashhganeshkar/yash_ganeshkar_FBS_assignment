

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

num = int(input("Enter Number = "))

for i in range(num, 0, -1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()