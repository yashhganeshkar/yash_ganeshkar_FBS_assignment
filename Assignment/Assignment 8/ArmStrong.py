
def count(num):
    count = 0
    while(num != 0):
        num = num // 10
        count += 1
    
    return count

def ArmStrong(num):
    temp = num
    addition = 0
    p = count(num)
    while(num != 0):
        r = num % 10
        num = num // 10
        addition += (r**p)
    
    if(temp == addition):
        return "ArmStrong Number"
    else:
        return "Not a ArmStrong Number"

num = int(input("Enter Number = "))

print(ArmStrong(num))