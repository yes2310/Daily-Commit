n = int(input())
num = list(map(int, input().split()))

isPrime = None
count = 0

for i in range(n):
    if num[i] == 1:
        isPrime = False
    else:
        isPrime = True

    for j in range(2, num[i]):
        if num[i] % j == 0:
            isPrime = False

    if isPrime == True:
        count += 1

print(count)
