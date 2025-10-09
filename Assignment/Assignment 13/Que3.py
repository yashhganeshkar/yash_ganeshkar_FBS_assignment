# Python Program to Check if a Given Key Exists in a Dictionary or Not

di = {
    "name": "Yashh",
    "Surname": "Ganeshkar",
    "age" : 21
}

target = input("Enter Your Target = ")

for key in di:
    if(target == key):
        print("Target Found")
        break
else:
    print("Target Not Found!")


