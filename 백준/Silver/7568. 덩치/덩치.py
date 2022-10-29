bulk = []

for _ in range(int(input())):
    bulk.append(list(map(int, input().split())))

for i in bulk:
    rank = 1

    for j in bulk:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1

    print(rank, end=" ")
