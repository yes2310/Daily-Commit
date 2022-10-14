import math

minInput = int(input())
maxInput = int(input())

primeNum = list(x for x in range(2, maxInput + 1))
sqrt = int(math.sqrt(maxInput))

for i in range(2, sqrt + 1):
    j = 2

    while i * j <= maxInput:
        try:
            primeNum.remove(i * j)
        except ValueError:
            pass
        
        j += 1

for k in range(len(primeNum)):
    if primeNum[0] < minInput:
        primeNum.remove(primeNum[0])

if len(primeNum) == 0:
    print(-1)
else:
    print(sum(primeNum))
    print(min(primeNum))
