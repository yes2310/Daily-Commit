n = int(input())
num = list(map(int, input().split()))

point = {}
i = 0

for j in sorted(num):
    if j not in point:
        point[j] = i
        i += 1

for k in num:
    print(point[k], end=" ")
