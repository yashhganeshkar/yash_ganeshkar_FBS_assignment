
# Create a class MedicalStudent inherited from Student with following:

    # i. Data members :Specialization
    # ii. MarksOfInternship
# b. Add the following methods :
    # i. Parameterized constructor
    # ii. Display
    # iii. Accept
    # iv. override Method CalculateRank
    # v. Override __str__ Method


class Student:
    def __init__(self,branch,InternalMarks):
        self.branch = branch
        self.InternalMarks = InternalMarks
    
    def Display(self):
        print(f"Branch = {self.branch}")
        print(f"Internal Marks = {self.InternalMarks}")

    def CalculateRank(self):
        if self.InternalMarks >= 90:
            return "A"
        elif self.InternalMarks >= 75:
            return "B"
        elif self.InternalMarks >= 60:
            return "C"
        elif self.InternalMarks >= 40:
            return "D"
        else:
            return "F"
    
    def Accept(self):
        self.branch = input("Enter Your Branch = ")
        self.InternalMarks = float(input("Enter Your Internal Marks"))
        print(Student.CalculateRank(self))
    
    def __str__(self):
        return f"Branch = {self.branch}\n Internal Marks = {self.InternalMarks}"


class MedicalStudent(Student):
    def __init__(self,Members,MarksofIntership):
        self.Members = Members
        self.internMakr = MarksofIntership
