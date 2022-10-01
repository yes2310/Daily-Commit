def hinsu(n):
    if n < 1000:
        a = n % 10
        b = n // 10 % 10
        c = n // 100 % 10

        if b - a == c - b:
            return True
    elif n == 1000:
        a = n % 10
        b = n // 10 % 10
        c = n // 100 % 10
        d = n // 1000 % 10

        if b - a == c - b == d - c:
            return True


count = 0

n = int(input())

for i in range(1, n + 1):
    if i < 100:
        count += 1
    else:
        if hinsu(i) == True:
            count += 1

print(count)
