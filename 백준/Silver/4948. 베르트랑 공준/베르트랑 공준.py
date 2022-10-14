def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False

        return True


def countPrime(n):
    count = 0

    for j in range(n + 1, n * 2 + 1):
        if isPrime(j):
            count += 1

    print(count)


while True:
    n = int(input())

    if n == 0:
        break
    else:
        countPrime(n)
