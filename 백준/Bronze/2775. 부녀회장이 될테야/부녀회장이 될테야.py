t = int(input())

for i in range(t):
    floor = int(input())
    num = int(input())

    zero = [i for i in range(1, num + 1)]

    for j in range(floor):
        for k in range(1, num):
            zero[k] += zero[k - 1]

    print(zero[-1])
