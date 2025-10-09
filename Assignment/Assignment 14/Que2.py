
# Write a Python program to remove the intersection of a second set with a first set.

s1 = {1,2,3,4}
s2 = {3,4,5,6}

s2.intersection_update(s1)

print(s2)