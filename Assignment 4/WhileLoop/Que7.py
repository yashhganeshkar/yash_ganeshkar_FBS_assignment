
# WAP to print all integers upto n that aren’t divisible by 2 and 3.

end = int(input("Enter Your Ending Number = "))

start = 1

while(start <= end):
    if((start%2 != 0) and (start%3 != 0)):
        print(start)
    start += 1