n = int(input())

soinsu = []

while n > 1:
    for i in range(2, n + 1):
        if n % i == 0:
            soinsu.append(i)
            n //= i
            break

for j in range(len(soinsu)):
    print(soinsu[j])
