white = [[0] * 100 for _ in range(100)]

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            white[j][k] = 1

count = 0

for l in range(100):
    for m in range(100):
        if white[l][m] == 1:
            count += 1

print(count)
