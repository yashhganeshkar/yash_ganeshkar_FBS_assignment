
#         A 
#       A B C 
#     A B C D E 
#   A B C D E F G 
# A B C D E F G H I 

num = int(input("Enter Your Number = "))

for i in range(1, num+1):
    ch = "A"
    for j in range(num-i):
        print(" ", end=" ")
    for k in range(1, i+1):
        print(ch, end=" ")
        ch = chr(ord(ch)+1)
    for a in range(1,i):
        print(ch, end=" ")
        ch = chr(ord(ch)+1)
    print()