
# Python Program to Add a Key-Value Pair to the Dictionary

count = int(input("How many entries you want to Enter = "))

di = {}

for i in range(1,count+1):
    key = input(f"Enter Key {i} = ")
    value = input(f"Enter value {i} = ")

    di[key] = value

print(di)