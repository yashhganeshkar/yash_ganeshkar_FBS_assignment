
# WAP to print all integers upto n that aren’t divisible by 2 and 3.

end = int(input("Enter Your Ending Number = "))

for num in range(1,end+1):
    if((num%2 != 0) and (num%3 != 0)):
        print(num)
