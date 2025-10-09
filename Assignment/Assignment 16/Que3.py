
# Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
    # j. Constructor (Support both parameterized and parameterless)
    # k. Destructor
    # l. ShowBook
    # m. For each size of shirt price should change by 10%.
    # (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and xlarge=1300) Use static concept.

class Shirt:
    def __init__(self,sid,sname,stype,price,size):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size
    
    def ShowShirt(self):
        print(f"Shirt ID = {self.sid}")
        print(f"Shirt Name = {self.sname}")
        print(f"Shirt Type = {self.stype}")
        print(f"Shirt Price = {self.price}")
        print(f"Shirt Size = {self.size}")
    
    def FinalPriceOfShirt(self):
        price = float(input("Enter Shirt Price = "))
        size = input("Enter Shirt Size (M:Medium,S:Small,X:xLarge) = ")

        if(size.lower() == 's'):
            print(f"Final Price of Shirt is = {price + (10/100)*price}")
        elif(size.lower() == 'm'):
            print(f"Final Price of Shirt is = {price + (10/100)*price}")
        elif(size.lower() == 'x'):
            print(f"Final Price of Shirt is = {price + (10/100)*price}")

    def __del__(self):
        pass

S = Shirt(1234,"Shirt","Formal",1299,"Medium")

S.FinalPriceOfShirt()