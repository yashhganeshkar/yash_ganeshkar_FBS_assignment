
#         1 
#       1 2 3 
#     1 2 3 4 5 
#   1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 8 9 

num = int(input("Enter Number = "))


for i in range(1, num+1):
    for j in range(num-i):
        print(" ", end=" ")
    for k in range(1,i+1):
        print(k, end=" ")
    count = k+1
    for a in range(1, i):
        print(count, end=" ")
        count += 1
    print()