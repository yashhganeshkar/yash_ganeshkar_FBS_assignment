
# Check triangle is equilateral isosceles or scalene

side1 = float(input("Enter Side 1 = "))
side2 = float(input("Enter Side 2 = "))
side3 = float(input("Enter Side 3 = "))

if(side1 == side2 == side3):
    print("Triangle are equilateral")
elif((side1 == side2) or (side1 == side3) or (side3 == side2)):
    print("Triangle is isosceles")
elif(side1 != side2 != side3):
    print("Triangle is scalene")
else:
    print("Can't Find Any Type of Triangle!")