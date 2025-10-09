
# Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

students = int(input("Enter Number of Students = "))

totalMarks = int(input("Enter Out of Marks = "))

for student in range(1,students + 1):
    name = input("Enter Student Name = ")
    addition = 0
    for sub in range(1,6):
        mark = int(input(f"Enter Your marks for subject {sub} = "))
        addition += mark
    percentage = (addition / totalMarks) * 100
    print(f"Student {name} got {percentage}%")