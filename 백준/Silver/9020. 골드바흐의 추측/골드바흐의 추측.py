def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True


repeat = int(input())

for i in range(repeat):
    n = int(input())

    a, b = n // 2, n // 2

    while a > 0:
        if isPrime(a) and isPrime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
