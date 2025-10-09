
# Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

amount = int(input("Enter the amount: "))
count = 0
i = 0

while amount > 0:
    if i == 0:
        note = 500
    elif i == 1:
        note = 200
    elif i == 2:
        note = 100
    elif i == 3:
        note = 50
    elif i == 4:
        note = 20
    elif i == 5:
        note = 10
    elif i == 6:
        note = 5
    elif i == 7:
        note = 2
    else:
        note = 1

    if amount >= note:
        count += amount // note
        amount = amount % note

    i += 1

print("Minimum number of notes needed:", count)
