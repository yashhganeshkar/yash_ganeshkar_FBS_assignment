
# Python Program to Calculate the Number of Words and the Number of Characters Present in a String

name = "Yashh Rajkumar Ganeshkar"

words = 1
char = 0

for i in name:
    if(i == " "):
        words += 1
    elif(i != " "):
        char += 1

print(f"Words = {words}")
print(f"Char = {char}")