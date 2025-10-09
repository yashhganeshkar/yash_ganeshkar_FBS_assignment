
# Python Program to Find the Second Largest Number in a List Using Bubble Sort

li = [5,8,2,1,9,7,10,2,55,21,25]

for ele in range(1, len(li)):
    for i in range(len(li)-ele):
        if(li[i] > li[i+1]):
            li[i], li[i+1] = li[i+1], li[i]

print(li[-2])