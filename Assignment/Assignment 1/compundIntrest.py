
principle = float(input("Enter Principle = "))
duration = int(input("Enter Duration in Years = "))
intrest = float(input("Enter Rate of Intrest = "))

amount = principle*((1+(intrest/100))**duration)

CI = amount - principle

print("Compound Intrest = ",CI)