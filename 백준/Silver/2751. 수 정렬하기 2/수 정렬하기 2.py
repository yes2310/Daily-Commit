import sys

temp = []

for i in range(int(sys.stdin.readline())):
    temp.append(int(sys.stdin.readline()))

temp.sort()

for j in range(len(temp)):
    print(temp[j])
