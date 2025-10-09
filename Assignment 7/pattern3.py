
#         * 
#       *   * 
#     *       * 
#   *           * 
# *               * 
#   *           * 
#     *       * 
#       *   * 
#         * 

num = int(input("Enter Number = "))

for i in range(1, num+1):
    for j in range(num-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        if((k==0) or (k == (2*i-2))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(num-1, 0, -1):
    for j in range(num-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        if((k==0) or (k == (2*i-2))):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()