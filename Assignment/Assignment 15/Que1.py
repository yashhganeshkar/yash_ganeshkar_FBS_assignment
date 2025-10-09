

# Create a class Book with members as bid,bname,price and author.Add following
# methods:
#     a. Constructor (Support both parameterized and parameterless)
#     b. Destructor
#     c. ShowBook

class Book:
    def __init__(self,bid="NA",bname="NA",price="NA",author="NA"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
    
    def ShowBook(self):
        print(f"Book ID = {self.bid}")
        print(f"Book Name = {self.bname}")
        print(f"Book Price = {self.price}")
        print(f"Book Author = {self.author}")
    
    def __del__(self):
        pass

B = Book("R-15346","You can Win",578,"Shiv Khera")

B.ShowBook()