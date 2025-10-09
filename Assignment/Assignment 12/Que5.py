
# Python Program to Count the Number of Vowels in a String

name = "Yashh Rajkumar Ganeshkar"
count = 0

for i in name:
    if(i in "aeiou"):
        count += 1

print(count)