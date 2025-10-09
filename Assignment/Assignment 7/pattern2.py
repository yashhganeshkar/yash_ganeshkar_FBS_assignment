
# 1 
# 1 2 
# 1   3 
# 1     4 
# 1 2 3 4 5 

num = int(input("Enter Number = "))

for row in range(1, num+1):
    for col in range(1, row+1):
        if(row==col or col == 1 or row == 5):
            print(col, end=" ")
        else:
            print(" ", end=" ")
    print()
