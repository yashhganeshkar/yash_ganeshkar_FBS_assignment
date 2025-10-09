
# Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator


class Distance:
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
        self.normalize()

    def __del__(self):
        print(f"Distance object {self.km} km, {self.m} m, {self.cm} cm is destroyed.")

    def to_centimeters(self):
        return self.km * 100000 + self.m * 100 + self.cm

    @staticmethod
    def from_centimeters(total_cm):
        km = total_cm // 100000
        total_cm %= 100000
        m = total_cm // 100
        cm = total_cm % 100
        return Distance(km, m, cm)

    def normalize(self):
        total_cm = self.to_centimeters()
        normalized = Distance.from_centimeters(total_cm)
        self.km = normalized.km
        self.m = normalized.m
        self.cm = normalized.cm

    def __add__(self, other):
        total_cm = self.to_centimeters() + other.to_centimeters()
        return Distance.from_centimeters(total_cm)

    def __sub__(self, other):
        total_cm = self.to_centimeters() - other.to_centimeters()
        if total_cm < 0:
            total_cm = 0  # Optional: or raise an error
        return Distance.from_centimeters(total_cm)

    def __str__(self):
        return f"{self.km} km, {self.m} m, {self.cm} cm"


d1 = Distance(1, 950, 80)
d2 = Distance(0, 100, 30)

print("Distance 1:", d1)
print("Distance 2:", d2)

d3 = d1 + d2
print("Addition:", d3)

d4 = d1 - d2
print("Subtraction:", d4)
