
# Write a program to solve the following series :

# a) 1! + 2! + 3! + 4! + .....n!

end = int(input("Enter Your End = "))

addFact = 0

for i in range(1,end+1):
    fact = 1
    for j in range(1,i+1):
        fact *= j
    addFact += fact

print(addFact)

# b) N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

num = int(input("Enter Your Number = "))

addition = 0

for i in range(1,num+1):
    addition += (num**i)

print(addition)

# c) Find the sum of a geometric series from 1 to n where the common ratio is 2.

n = int(input("Enter the number of terms (n): "))

sum_of_series = (2 ** n) - 1

print("Sum of the geometric series is:", sum_of_series)

# d) S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a = int(input("Enter a number = "))

addition = 0

for i in range(1,a+1):
    addition += (a*i)/i

print(addition)


# e) x - x2/3 + x3/5 - x4/7 + .... to n terms

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))

sum_series = 0
sign = 1  

for i in range(n):
    power = i + 1
    denominator = 2 * i + 1  
    term = sign * (x ** power) / denominator
    sum_series += term
    sign *= -1  
print("Sum of the series is:", sum_series)
