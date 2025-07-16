
num = int(input("Enter Number = "))

i = 1

while(i <= num):
    if(i % 7 == 0 and i % 5 == 0):
        print(i)
    i += 1