import sys

num = list(0 for x in range(0, 10001))

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    num[n] += 1

for i in range(len(num)):
    if num[i] > 0:
        for j in range(num[i]):
            print(i)
