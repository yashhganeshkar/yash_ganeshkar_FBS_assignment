# Python Program to Sort a List According to the Length of the Elements within the list.

elements = ["Ganeshkar","Yashh","Rajkumar"]

for ele in range(1, len(elements)):
    for i in range(len(elements)-ele):
        if(len(elements[i]) > len(elements[i+1])):
            elements[i], elements[i+1] = elements[i+1],elements[i]

print(elements)