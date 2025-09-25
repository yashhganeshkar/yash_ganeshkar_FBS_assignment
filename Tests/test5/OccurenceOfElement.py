
num = [1,3,4,1,2,3,6,7,1,2,4]

di = {}

for i in range(len(num)):
    if(num[i] not in di):
        di[num[i]] = 1
    else:
        di[num[i]] += 1

print(di)