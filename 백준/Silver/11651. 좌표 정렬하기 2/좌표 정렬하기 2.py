import sys

point = []

n = int(sys.stdin.readline())

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    point.append([x, y])


point.sort(key=lambda x: (x[1], x[0]))

for j in range(n):
    print(*point[j])
