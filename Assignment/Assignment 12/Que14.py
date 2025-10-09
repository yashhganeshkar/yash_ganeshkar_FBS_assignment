
# Python Program to count number of digits and letters in a string.

name = "Yashh Ganeshkar"

for i in name:
    count = 0
    for j in name:
        if(i==j):
            count += 1
    print(f"Count of {i} is {count}")