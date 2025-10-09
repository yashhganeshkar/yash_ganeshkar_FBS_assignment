
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

num = int(input("Enter Number = "))

for i in range(1, num+1):
    for j in range(num-i,0,-1):
        print(" ", end=" ")
    for k in range(1, i+1):
        print("*", end=" ")
    for l in range(1,i):
        print("*", end=" ")

    print()

