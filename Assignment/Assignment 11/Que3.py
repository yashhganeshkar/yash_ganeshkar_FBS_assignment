
# Python Program to Sort the List According to the Second Element in Sublist

li = [[1, 4], [3, 1], [5, 2]]

for ele in range(1,len(li)):
    for i in range(len(li)-ele):
        if(li[i][1] > li[i+1][1]):
            li[i], li[i+1] = li[i+1], li[i]

print(li)