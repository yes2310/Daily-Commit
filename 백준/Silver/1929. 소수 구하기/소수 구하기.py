def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True


minInput, maxInput = map(int, input().split())

for j in range(minInput, maxInput + 1):
    if isPrime(j):
        print(j)
