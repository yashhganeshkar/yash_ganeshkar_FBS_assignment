

# Create a class Book with members as bid,bname,price and author.Add following
# methods:
    # a. Constructor (Support both parameterized and parameterless)
    # b. Destructor
    # c. ShowBook
    # d. Add static variable count and also maintain count of objects created.

class Book:

    count = 0

    def __init__(self,bid,bname,price,author):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1

    def ShowBook(self):
        print(f"Book ID = {self.bid}")
        print(f"Book Name = {self.bname}")
        print(f"Book Price = {self.price}")
        print(f"Book Author = {self.author}")
    
    def __del__(self):
        pass

B1 = Book("R-15346","You can Win",578,"Shiv Khera")
B2 = Book("R-15346","You can Win",578,"Shiv Khera")

print(B2.count)