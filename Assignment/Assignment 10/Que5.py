
# Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

li = []

total = int(input("Enter the Number of elements You want to add in list = "))

for num in range(1,total+1):
    element = int(input(f"Enter Number {num} = "))
    li.append(element)

target = int(input("Enter the Target = "))

for num in li:
    if(target == num):
        print("Target Found!")
        count = 0
        for i in li:
            if(target == i):
                count += 1
        print(f"Target Present in List {count} Times")
        break
else:
    print("Target Not Found!")