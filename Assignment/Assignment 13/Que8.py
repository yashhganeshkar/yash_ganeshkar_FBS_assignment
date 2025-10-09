
# Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

name = "Yashh Ganeshkar"

di = {}

for i in name:
    if(i not in di):
        di[i] = 1
    else:
        di[i] += 1

print(di)