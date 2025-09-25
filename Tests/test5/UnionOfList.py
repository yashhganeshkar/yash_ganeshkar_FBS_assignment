
li1 = [1,2,3,4,5]
li2 = [4,5,6,7,8]

l3 = li1 + li2

union_set = []

for i in l3:
    if(i not in union_set):
        union_set.append(i)

print(union_set)