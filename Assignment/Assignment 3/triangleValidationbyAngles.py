
# Check a Valid Triangle by Angle

angle1 = float(input("Enter Angle 1 = "))
angle2 = float(input("Enter Angle 2 = "))
angle3 = float(input("Enter Angle 3 = "))

sumOfAngle = angle1 + angle2 + angle3

if(sumOfAngle == 180):
    print("Triangle is Valid")
else:
    print("Triangle is Not Valid")
