
#Find Area and perimeter of following figure

lenght = float(input("Enter Length = "))
breadth = float(input("Enter Breadth = "))
radius = float(input("Enter Radius = "))

AreaOfReactangle = lenght * breadth
PerimeterOfReactangle = (2 * lenght) + breadth

AreaOfCircle = 3.14*(radius * radius)
PerimeterOfCircle = 3.14*radius 

AreaOfGivenFigure = AreaOfReactangle + (AreaOfCircle / 2)
PerimeterOfGivenFigure = PerimeterOfReactangle + (PerimeterOfCircle / 2)

print("Area Of Given Figure = ", AreaOfGivenFigure)
print("Perimeter Of Given Figure = ", PerimeterOfGivenFigure)
