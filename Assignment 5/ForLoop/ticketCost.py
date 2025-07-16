
numOfPassenger = int(input("Enter Number of Passanger = "))
ticketPrice = int(input("Enter Ticket Price = "))

totalTicket = 0

for i in range(1, numOfPassenger+1):
    age = int(input(f"Enter Age of Person {i} ="))

    if(age < 12):
        discountTicket = (70/100) * ticketPrice
        totalTicket += discountTicket
    elif(age > 59):
        discountTicket = (50/100) * ticketPrice
        totalTicket += discountTicket
    else:
        totalTicket += ticketPrice

print(totalTicket)