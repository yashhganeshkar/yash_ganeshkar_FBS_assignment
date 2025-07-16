
start = int(input("Enter Start = "))
stop = int(input("Enter Stop = "))

for i in range(start, stop+1):
    is_prime = True
    for j in range(2, int(i * 0.5) + 1):
        if(i % j == 0):
            is_prime = False
            break
    if is_prime:
        print(i)