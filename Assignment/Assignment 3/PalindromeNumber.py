
num = int(input("Enter Your Number = "))

rev_num = int(str(num)[::-1])

if(num == rev_num):
    print("Palindrome number")
else:
    print("Not an Palindrome Number")