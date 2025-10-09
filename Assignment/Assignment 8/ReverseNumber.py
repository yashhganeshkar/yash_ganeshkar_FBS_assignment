
def RevNum(num):
    Revnum = 0

    while(num != 0):
        r = num % 10
        num = num // 10

        Revnum = (Revnum * 10) + r
    
    return Revnum

num = int(input("Enter Number = "))

print(RevNum(num))