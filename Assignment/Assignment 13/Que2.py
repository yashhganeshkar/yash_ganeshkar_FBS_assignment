
# Python Program to Concatenate Two Dictionaries Into One

di = {
    "name": "Yashh",
    "age" : 21
}

di2 = {
    "Fname": "Tejas",
    "Tage" : 22
}


for key,value in di2.items():
    di[key] = value

print(di)