
# Find all of the words in a string that are less than 5 letters (take input from user)

name = input("Ente Your String = ")

result = [i for i in name.split(' ') if(len(i) < 5)]

print(result)