
# Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

end = int(input("Enter Your Ending number = "))

di = {}

for i in range(1,end+1):
    di[i] = i*i

print(di)