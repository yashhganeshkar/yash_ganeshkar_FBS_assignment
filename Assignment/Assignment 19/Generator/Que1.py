
# We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.

def FibbSeries(num):
    prev1 = 0
    prev2 = 1

    for i in range(1,num+1):
        if(i>2):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
            yield current
        elif(i==1):
            yield prev1
        elif(i==2):
            yield prev2

num = int(input("How Many Numbers Your want to Generate = "))

fibb = FibbSeries(num)

for i in range(1,num+1):
    print(next(fibb))