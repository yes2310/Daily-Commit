import sys

point = []

n = int(sys.stdin.readline())

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    point.append([x, y])


point.sort()

for j in range(n):
    print(*point[j])
