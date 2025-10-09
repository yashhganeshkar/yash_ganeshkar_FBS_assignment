
# Write a Python program to find elements in a given set that are not n another set.

s1 = {1,2,3,4}
s2 = {3,4,5,6}

for i in s1:
    if(i not in s2):
        print(i)
