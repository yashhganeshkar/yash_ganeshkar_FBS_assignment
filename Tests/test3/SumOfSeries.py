
N = int(input("Enter N value = "))

addition = 0

for i in range(1, N+1):
    
    fact = 1
    fact *= i
    addition += i/fact

print(addition)