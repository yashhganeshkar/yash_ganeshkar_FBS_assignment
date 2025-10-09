
# Python Program to Remove the Given Key from a Dictionary

key = int(input("Enter the Key = "))

di = {
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5
}

for i in di:
    if(i==key):
        del di[i]
        break

print(di)