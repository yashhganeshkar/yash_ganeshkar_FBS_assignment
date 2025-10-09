
# Create a class College which has collection of students. Add the
# following methods :
    # a. Parameteried constructor for number of students.
    # b. AddStudent
    # c. GetStudent
    # d. RemoveStudent
    # e. Override __str__ Method

class Student:
    def __init__(self, student_id, name, age, percentage):
        self.StudentId = student_id
        self.Name = name
        self.Age = age
        self.Percentage = percentage

    def Display(self):
        print("Student ID:", self.StudentId)
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("Percentage:", self.Percentage)

    def Accept(self):
        self.StudentId = input("Enter Student ID: ")
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    def CalculateRank(self):
        if self.Percentage >= 90:
            return "A"
        elif self.Percentage >= 75:
            return "B"
        elif self.Percentage >= 60:
            return "C"
        elif self.Percentage >= 40:
            return "D"
        else:
            return "F"

    def __str__(self):
        return f"Student[ID={self.StudentId}, Name={self.Name}, Age={self.Age}, Percentage={self.Percentage}]"

# College class
class College:
    def __init__(self, num_students):
        self.students = []
        self.capacity = num_students

    def AddStudent(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
        else:
            print("Cannot add more students. Capacity full.")

    def GetStudent(self, student_id):
        for student in self.students:
            if student.StudentId == student_id:
                return student
        return None

    def RemoveStudent(self, student_id):
        for student in self.students:
            if student.StudentId == student_id:
                self.students.remove(student)
                return True
        return False

    def __str__(self):
        result = f"College has {len(self.students)} student(s):\n"
        for student in self.students:
            result += str(student) + "\n"
        return result
