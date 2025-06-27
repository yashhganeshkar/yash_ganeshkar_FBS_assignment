
num = int(input("ENter 3 Digit Number = "))

#234

a = num % 10 #4
num = num // 10 #23
b = num % 10 #3
c = num // 10 #2

rev = (a*100)+(b*10)+c

print(rev)
