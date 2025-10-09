
# WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

start = int(input("Enter Your Starting Number = "))
end = int(input("Enter Your ending Number = "))

for num in range(start, end+1):
    if(num%7 == 0 and num%5 == 0):
        print(num)