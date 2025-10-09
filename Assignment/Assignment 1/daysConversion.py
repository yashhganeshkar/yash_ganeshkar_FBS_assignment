
#Take an input from User in a days and convert into years, weeks and days

days = int(input("Enter Days = "))

years = days // 365

remainingDays = days % 365

weeks = remainingDays // 7

remainingDays = remainingDays % 7

print("Years = ", years)
print("weeks = ", weeks)
print("Days = ", remainingDays)
