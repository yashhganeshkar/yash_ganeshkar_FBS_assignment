
# Python Program to Detect if Two Strings are Anagrams

str1 = input("Enter String 1 = ")
str2 = input("Enter String 2 = ")

if(len(str1) == len(str2)):
    for i in range(len(str1)):
        if((str1[i] not in str2) or (str2[i] not in str1)):
            print("Not an Anagram")
            break
    else:
        print("Anagram")
else:
    print("Not an Anagram String")