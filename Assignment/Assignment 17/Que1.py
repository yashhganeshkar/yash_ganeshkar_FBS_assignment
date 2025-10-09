
# 1. Create a class Student with following
    # a. data members :
        # i. StudentId
        # ii. Name
        # iii. Age
        # iv. Percentage
    # b. Add the following methods :
        # i. Parameterized constructor
        # ii. Display
        # iii. Accept
        # iv. Method CalculateRank
        # v. Override __str__ Method

class Student:
    def __init__(self,studentId,name,age,percentage):
        self.studentID = studentId
        self.name = name
        self.age = age
        self.percentage = percentage
    
    def Display(self):
        print(f"Student ID = {self.studentID}")
        print(f"Student Name = {self.name}")
        print(f"Student age = {self.age}")
        print(f"Student Percentage = {self.percentage}")
    
    def CalculateRank(self):
        if self.percentage >= 90:
            return "A"
        elif self.percentage >= 75:
            return "B"
        elif self.percentage >= 60:
            return "C"
        elif self.percentage >= 40:
            return "D"
        else:
            return "F"
        
    def Accept(self):
        self.studentID = input("Enter Your Student ID = ")
        self.name  = input("Enter Your Student Name = ")
        self.age = int(input("Enter Your Age"))
        self.percentage = float(input("Enter Your Percentage = "))
        print(Student.CalculateRank(self))
    
    def __str__(self):
        return f"StudentID = {self.studentID}\nName = {self.name}\nAge = {self.age}\nPercentage = {self.percentage}"

S = Student("1234","Yashh",21,90)

S.Display()

print(S.CalculateRank())

S.Accept()