
admin = "yashhganeshkar"
adminPassword = "yashh@123"

for i in range(1,4):

    userId = input("Enter Username = ")
    password = input("Enter Password = ")

    if((userId == admin) and (password == adminPassword)):
        print("Welcome, ", admin)
        break
    else:
        print("Wrong Credentials! Try Again...")
        continue