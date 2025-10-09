
# Remove all of the vowels in a string (take input from user)

string = input("enter Your strings = ")

removeVowels = ''.join([i for i in string if(i not in "aeiou")])

print(removeVowels)