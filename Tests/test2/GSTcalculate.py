
# Calculate Total Bill including GST

product1 = float(input("Enter Price of Product 1 = "))
product2 = float(input("Enter Price of Product 2 = "))
product3 = float(input("Enter Price of Product 3 = "))
product4 = float(input("Enter Price of Product 4 = "))
product5 = float(input("Enter Price of Product 5 = "))

bill = product1 + product2 + product3 + product4 + product5

finalBill = bill + ((18/100)*bill)

print("Your Final Bill inlcuding GST = ", finalBill)
