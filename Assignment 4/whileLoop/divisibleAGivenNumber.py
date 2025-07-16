
start = int(input("Enter Your start = "))
stop = int(input("Enter Your stop = "))

num = int(input("Enter Your num = "))

while(start <= stop):
    if(start % num == 0):
        print(start)
    
    start += 1