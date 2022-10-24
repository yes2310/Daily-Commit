x, y = map(int, input().split())

a = []
b = []

for i in range(x):
    a.append(list(map(int, input().split())))


for j in range(x):
    b.append(list(map(int, input().split())))

for k in range(x):
    for l in range(y):
        print(a[k][l] + b[k][l], end=" ")
    print()
