
# Count the number of spaces in a string (take input from user)

string = input("Enter Your String Here = ")

spaces = len([i for i in string if(i == " ")])

print(spaces)