
# Python Program to Merge Two Lists and Sort it

li1 = [5,8,2,1,9]
li2 = [7,10,2,55,21]

sortList = li1+li2

for ele in range(1,len(sortList)):
    for i in range(len(sortList) - ele):
        if(sortList[i] > sortList[i+1]):
            sortList[i], sortList[i+1] = sortList[i+1], sortList[i]

print(sortList)