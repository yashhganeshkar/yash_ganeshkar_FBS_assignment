
# WAP to print all numbers in a range divisible by a given number.

start = int(input("Enter Your Starting Number = "))
end = int(input("Enter Your ending Number = "))

div = int(input("Enter Your Number = "))

while(start <= end):
    if(start % div == 0):
        print(start)
    start += 1