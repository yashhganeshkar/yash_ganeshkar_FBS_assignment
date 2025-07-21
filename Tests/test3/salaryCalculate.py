
emp = int(input("How many Employee salary You Want to Check = "))

count = 1

AllEmpSalary = 0

while(count <= emp):
    basicPay = float(input(f"Enter Your Base salary of Employee {count} = "))

    if(basicPay < 20000):
        da = (10/100) * basicPay
        ta = (12/100) * basicPay
        hra = (15/100) * basicPay
    else:
        da = (15/100) * basicPay
        ta = (18/100) * basicPay
        hra = (20/100) * basicPay
    
    totalSalary = basicPay+da+ta+hra
    print(f"Total Salary of Employee {count} is {totalSalary}")
    count += 1
    AllEmpSalary += totalSalary

print(f"Total Salary of All Employee is {AllEmpSalary}")