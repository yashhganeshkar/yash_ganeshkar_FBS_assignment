
# Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

count = 0

while(True):
    user = input("Enter Username = ")
    password = input("Enter Password = ")
    
    if(user == "yashh" and password == "yashh123"):
        print("Login Successfully")
    else:
        count += 1
        if(count == 3):
            break
        continue
