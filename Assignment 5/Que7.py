
# Write a program to print first n prime numbers.

end = int(input("Enter Your Number = "))

for num in range(2,end+1):
    for i in range(2,num):
        if(num%i == 0):
            break
    else:
        print(num)