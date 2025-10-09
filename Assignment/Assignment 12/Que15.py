
# Python Program to find larger string without using built-in functions.

def LargerString(*strings):
    di = {}
    for i in strings:
        count = 0
        for j in i:
            count += 1
        di[i] = count
    
    max_value = 0
    max_str = ""

    for key in di:
        if(di[key] > max_value):
            max_value = di[key]
            max_str = key
    
    print(max_str)


name = "Yashh"
middleName = "Rajkumar"
surname = "Ganeshkar"

LargerString(name,middleName,surname)