
# Python Program to count number of lowercase characters in a string.

name = "Yashh GanesHkaR"

count = 0

for i in name:
    if(97 <= ord(i) <= 122):
        count += 1

print(count)