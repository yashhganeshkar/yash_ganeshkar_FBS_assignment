
# A 
# A B 
# A B C 
# A B C D 
# A B C D E 

num = int(input("Enter Your Number = "))

for i in range(1, num+1):
    ch = "A"
    for j in range(1, i+1):
        print(ch, end=" ")
        ch = chr(ord(ch)+1)
    print()