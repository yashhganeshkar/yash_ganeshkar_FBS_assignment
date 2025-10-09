
# Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
    # f. Destructor
    # g. ShowBook
    # h. Add static member discount.
    # i. Provide methods for applying discount on price of product.

class Product:
    def __init__(self,pid="NA",pname="NA",price="NA",quantity="NA"):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
    
    @staticmethod
    def Discount():
        price = float(input("Enter Your Price = "))
        discountPer = float(input("Enter Your Percentage for discount = "))
        print(f"Your Final Price is = {price - (discountPer/100)*price}")

    def ProductDiscount(self,discountPer):
        print(f"Your Final Price is = {self.price - (discountPer/100)*self.price}")

    def ShowProduct(self):
        print(f"Product ID = {self.pid}")
        print(f"Product Name = {self.pname}")
        print(f"Product Price = {self.price}")
        print(f"Product Author = {self.quantity}")
    
    def __del__(self):
        pass

P = Product(1234,"Marker",25000,10)

P.ProductDiscount(30)

P.Discount()