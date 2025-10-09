
# WAP to print all even numbers until n.

end = int(input("Enter Your Ending Number = "))

start = 1

while(start <= end):
    if(start %2 == 0):
        print(start)
    start += 1