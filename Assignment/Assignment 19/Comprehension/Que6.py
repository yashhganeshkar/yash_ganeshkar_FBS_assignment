
# Use a dictionary comprehension to count the length of each word in a sentence (take input from user)

string = input("Enter Your string Here = ")

di = {i:len(i) for i in string.split(' ')}

print(di)