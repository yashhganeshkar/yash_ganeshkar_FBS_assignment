
# Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator


class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __del__(self):
        print(f"ComplexNumber object with value {self.real} + {self.imag}i is destroyed.")

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


c1 = ComplexNumber(4, 5)
c2 = ComplexNumber(2, 3)

print("First complex number:", c1)
print("Second complex number:", c2)

c3 = c1 + c2
print("Addition:", c3)

c4 = c1 - c2
print("Subtraction:", c4)