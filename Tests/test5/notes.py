
amount = int(input("Enter Your Total Amount = "))

print(f"Your Total Amount is {amount}")

notes = [2000, 500, 200, 100 , 50, 20, 10, 5]

for i in range(len(notes)):
    count = amount // notes[i]
    amount -= (notes[i]*count)
    print(f"{notes[i]} = {count}")