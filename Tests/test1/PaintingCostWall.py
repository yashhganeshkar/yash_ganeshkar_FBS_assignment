
side = float(input("Enter Sides of a Room = "))

costInner = float(input("Enter Cost For Inner Area (per Sq) = "))

costOuter = float(input("Enter Cost For Outer Area (per Sq)= "))

totalArea = 4*side*side

totalCost = (totalArea*costInner) + (totalArea*costOuter)

print("Payable Amount = ",2*totalCost)