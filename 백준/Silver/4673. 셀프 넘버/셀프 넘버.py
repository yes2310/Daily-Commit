def d(n):
    n = str(n)
    sum = 0

    for i in range(len(n)):
        sum += int(n[i])

    return int(n) + sum


not_self_number = []
self_number = list(range(1, 10001))

for i in range(1, 10001):
    not_self_number.append(d(i))

for i in range(len(not_self_number)):
    try:
        self_number.remove(not_self_number[i])
    except ValueError:
        pass

for i in range(len(self_number)):
    print(self_number[i])
