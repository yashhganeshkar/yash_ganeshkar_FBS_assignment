
# Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
#     d. Constructor (Support both parameterized and parameterless)
#     e. Destructor
#     f. ShowBook

class Product:
    def __init__(self,pid="NA",pname="NA",price="NA",quantity="NA"):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
    
    def ShowProduct(self):
        print(f"Product ID = {self.pid}")
        print(f"Product Name = {self.pname}")
        print(f"Product Price = {self.price}")
        print(f"Product Author = {self.quantity}")
    
    def __del__(self):
        pass

P = Product(1234,"Marker",25,10)

P.ShowProduct()