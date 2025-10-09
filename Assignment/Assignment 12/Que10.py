
# Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions

str1 = "Yashh"
str2 = "Ganeshkar"

len_str1 = 0
len_str2 = 0

for i in str1:
    len_str1 += 1

for j in str2:
    len_str2 += 1

if(len_str1 > len_str2):
    print(f"{str1} is greatest")
else:
    print(f"{str2} is greatest")