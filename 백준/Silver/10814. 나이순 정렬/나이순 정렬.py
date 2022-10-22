n = int(input())

sortAge = []

for i in range(n):
    age, name = input().split()
    sortAge.append([int(age), name])

sortAge.sort(key=lambda x: x[0])

for j in range(n):
    print(*sortAge[j])
