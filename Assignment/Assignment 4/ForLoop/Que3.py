
# WAP to print sum of series upto n.

end = int(input("Enter Your Ending Number = "))

addition = 0

for num in range(1,end+1):
    addition += num

print(f"Addition of Series is {addition}")