
# WAP to print all odd numbers until n.

end = int(input("Enter Your Ending Number = "))

for num in range(1,end+1):
    if(num%2 != 0):
        print(num)
