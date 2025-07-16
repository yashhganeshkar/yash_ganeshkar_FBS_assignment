
numOfStudent = int(input("Enter Number of Students = "))

for i in range(1, numOfStudent+1):
    percentage = 0
    for j in range(1,6):
        marks = float(input(f"Enter Mark of Subject {j} = "))
        percentage += marks
    
    print(f"Student {i} = {(percentage / 500)*100}")