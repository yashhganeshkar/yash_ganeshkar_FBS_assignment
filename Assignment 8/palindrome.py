
def PalindromeCheck(num):
    temp = num
    RevNum = 0

    while(num!=0):
        r = num % 10
        num = num // 10

        RevNum = (RevNum * 10) + r

    if(temp == RevNum):
        return "Palindrome"
    else:
        return "Not Palindrome"
    
num = int(input("Enter Number = "))

print(PalindromeCheck(num))
