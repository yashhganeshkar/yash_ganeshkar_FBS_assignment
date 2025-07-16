
start = int(input("Enter where to Start = "))
stop = int(input("Enter where to Stop = "))

num = int(input("Enter a Number to check Divisile Numbers = "))


for i in range(start, stop + 1):
    if(i % num == 0):
        print(i)
