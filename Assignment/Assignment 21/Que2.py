
# Create class television that has members to hold the model number ,screen size
# and price. Take a member function to take input from user, If more than 4 digits
# are entered for model number, if screen size is smaller than 12 inches or greater
# than 70 inches or if the price is negative or greater than 5000 Rs, then throw an
# exception.
# Write a main() that instantiates an object and allows the user to enter and display
# data. If exception is caught, replace all data member values with zero

class Television:
    def __init__(self):
        self.model_num = 0
        self.screen_size = 0
        self.price = 0
    
    def Member(self):
        try:
            self.model_num = int(input("Enter Your Model Number = "))
            if(len(str(self.model_num)) > 4):
                raise ValueError("Model number must be at most 4 digits")

            self.screen_size = int(input("Enter Your Screen Size = "))
            if(12 > self.screen_size > 70):
                raise ValueError("Screen size must be between 12 and 70 inches.")
            
            self.price = float(input("Enter TV Price = "))
            if(0 > self.price > 5000):
                raise ValueError("Price must be between 0 and 5000.")
            
        except Exception as e:
            print(e)
            self.model_num = 0
            self.screen_size = 0
            self.price = 0

    def display(self):
        print(f"Model Number: {self.model_num}")
        print(f"Screen Size: {self.screen_size}")
        print(f"Price: {self.price}")


if(__name__ == "__main__"):
    tv = Television()
    tv.Member()
    tv.display()