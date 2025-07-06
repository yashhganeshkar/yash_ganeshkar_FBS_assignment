
# Check a Valid Triangle by Sides

side1 = float(input("Enter Side 1 = "))
side2 = float(input("Enter Side 2 = "))
side3 = float(input("Enter Side 3 = "))

if(((side1 + side2) > side3) or ((side1 + side3) > side2) or ((side2 + side3) > side1)):
    print("Triangle is Valid!")
else:
    print("Triangle is Not Valid!")