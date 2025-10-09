
# Python Program to count number of digits and letters in a string.

name = "Yashh1234_@"

countDigits = 0
countLetters = 0

for i in name:
    if((65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 )):
        countLetters += 1
    elif(48 <= ord(i) <= 57):
        countDigits += 1

print("Digits = ",countDigits)
print("Letters = ",countLetters)
