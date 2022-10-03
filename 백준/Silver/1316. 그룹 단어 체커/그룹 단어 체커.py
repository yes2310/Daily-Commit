n = int(input())

world = [None] * n

for i in range(n):
    world[i] = input()

for i in range(n):
    temp = world[i]
    for j in range(len(temp)):
        for k in range(1, len(temp)):
            if temp[j] == temp[k]:
                if temp[k - 1] == temp[k]:
                    continue
                elif k - j > 1:
                    world[i] = None

world = list(filter(None, world))

print(len(world))
