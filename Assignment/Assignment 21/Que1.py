
# Develop a simple calculator program that performs basic arithmetic operations (+,
# -, *, /) on two numbers provided by the user. The program should ask the user for
# the numbers and the operator. However, the program should handle the following
# exceptions:
# a. Invalid Number: If the user enters a number that is not valid, catch the
# exception and display an error message.
# b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
# "/", catch the exception and display an error message.
# c. Division by Zero: If the user tries to divide by zero, catch the exception and
# display an error message.
# Write a program that performs the requested arithmetic operation and
# handles the exceptions as described above.

try:
    num1 = float(input("Enter Your Number 1 = "))
    num2 = float(input("Enter Your Number 2 = "))
    operator = input("Enter Operator (+,-,*,/) = ")
    if(operator.strip() not in "+-*/"):
        raise ValueError
    
    if(operator.strip() == "+"):
        print(f"Sum of {num1} and {num2} is {num1+num2}")
    elif(operator.strip() == "-"):
        print(f"Substraction of {num1} and {num2} is {num1-num2}")
    elif(operator.strip() == "*"):
        print(f"Multiplication of {num1} and {num2} is {num1*num2}")
    elif(operator.strip() == "/"):
        try:
            print(f"Division of {num1} and {num2} is {num1/num2}")
        except ZeroDivisionError:
            print("You can't Divide any number by zero, change Your Number 1!")
except ValueError:
    print("Enter a Valid Number")