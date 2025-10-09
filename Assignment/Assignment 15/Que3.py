
# Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
#     g. Constructor (Support both parameterized and parameterless)
#     h. Destructor
#     i. ShowBook

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
    
    def __del__(self):
        pass

S = Shirt(1234,"Shirt","Formal",1299,"Medium")

S.ShowShirt()