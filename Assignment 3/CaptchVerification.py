
# Accept UserId and Password. Also Check the Captcha

import random

userId = input("Enter Username = ")
password = input("Enter Password = ")

admin = "yashhganeshkar"
adminPassword = "yashh123"

if((userId == admin) and (password == adminPassword)):
    captcha = random.randint(1000, 9999)
    print("User Entered Correct Credentials")
    print("Your Captcha Was = ", captcha)
    userEnteredCaptcha = int(input("Please Enter Captcha given proceed further = "))
    if(captcha == userEnteredCaptcha):
        print("Captcha Was correct!")
        print(f"Welcome, {userId}")
    else:
        print("Wrong Captcha!")
else:
    print("Please Enter Correct Credentials!")