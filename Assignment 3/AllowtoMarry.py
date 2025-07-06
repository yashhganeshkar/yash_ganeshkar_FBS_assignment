
# Eligible to Marry or Not

gender = input("Enter Your Gender (M/F) = ")
age = int(input("Enter Your Age = "))

if(gender == "M"):
    if(age >= 21):
        print("You are Eligible to Marry")
    else:
        print("You are Not Eligible to Marry")
elif(gender == "F"):
    if(age >= 18):
        print("You are Eligible to Marry")
    else:
        print("You are Not Eligible to Marry")
else:
    print("Enter a valid Gender!")