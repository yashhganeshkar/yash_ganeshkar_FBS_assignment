
# WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

start = int(input("Enter Your Starting Number = "))
end = int(input("Enter Your ending Number = "))

while(start <= end):
    if((start%7==0) and (start%5==0)):
        print(start)
    start += 1