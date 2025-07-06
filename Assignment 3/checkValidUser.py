
# Check Valid UserId and Password

userId = input("Enter your User ID = ")
password = input("Enter Your Password = ")

admin = "yashhganeshkar"
adminPassword = "yashh123"

if((userId == admin) and (password == adminPassword)):
    print("UserId and Password Entered by user is Correct")
else:
    if(userId != admin):
        print("User Entered Wrong Username!")
    else:
        print("User Entered Wrong Password!")
    