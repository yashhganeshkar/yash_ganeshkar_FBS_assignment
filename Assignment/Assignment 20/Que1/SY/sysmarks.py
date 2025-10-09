

class SYMARKS:
    def __init__(self, computer_total=0, maths_total=0, electronics_total=0):
        self.ComputerTotal = computer_total
        self.MathsTotal = maths_total
        self.ElectronicsTotal = electronics_total

    def display_marks(self):
        print("Computer Total:", self.ComputerTotal)
        print("Maths Total:", self.MathsTotal)
        print("Electronics Total:", self.ElectronicsTotal)

    def get_total(self):
        return self.ComputerTotal + self.MathsTotal + self.ElectronicsTotal

    def __str__(self):
        return f"SYMARKS(Computer={self.ComputerTotal}, Maths={self.MathsTotal}, Electronics={self.ElectronicsTotal})"
