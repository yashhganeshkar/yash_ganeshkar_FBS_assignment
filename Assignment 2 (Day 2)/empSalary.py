
basicSalary = float(input("Enter Your Basic Salary = "))

da = ((10/100)*basicSalary)
ta = ((12/100)*basicSalary)
hra = ((15/100)*basicSalary)

totalSalary = basicSalary + da + ta + hra
print(totalSalary)