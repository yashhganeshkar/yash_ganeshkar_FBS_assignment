
num = int(input("Enter Your Number = "))

for i in range(2, num+1):
    is_prime = True
    for j in range(2, int(i * 0.5) + 1):
        if(j % j == 0):
            is_prime = False
            break
    if(is_prime):
        print(i)