
# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
#     a. Children below 12 = 30% discount
#     b. Senior citizen (above 59) = 50% discount
#     c. Others need to pay full.


passengers = int(input("Enter Number of Passengers = "))

ticket = int(input(f"Enter Ticket Price for Passengers = "))

for age in range(1,passengers+1):
    age = int(input(f"Enter Age of Passenger {age} = "))

    if(age < 12):
        finalFair = ticket - ((30/100) * ticket)
        print(f"Final Fair for Passenger {age} is = {finalFair}")
    elif(age > 59):
        finalFair = ticket - ((50/100) * ticket)
        print(f"Final Fair for Passenger {age} is = {finalFair}")
    else:
        finalFair = ticket
        print(f"Final Fair for Passenger {age} is = {finalFair}")