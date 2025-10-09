
costPrice = float(input("Enter Cost Price = "))
markPrice = float(input("Enter Mark Price = "))
discount = float(input("Enter Discount (If Applicable) = "))

sellingPrice = (markPrice - ((discount/100)*markPrice))

print("Selling Price = ",sellingPrice)