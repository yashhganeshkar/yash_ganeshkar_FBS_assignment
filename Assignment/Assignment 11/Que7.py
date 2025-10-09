
# Python Program to Find the Intersection of Two Lists

li1 = [1, 2, 3, 4]
li2 = [3, 4, 5, 6]

intersection = []

for ele in li1:
    if(ele in li2):
        intersection.append(ele)

print(intersection)