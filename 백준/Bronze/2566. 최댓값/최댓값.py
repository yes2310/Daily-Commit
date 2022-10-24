num = []

for i in range(9):
    num.append(list(map(int, input().split())))

temp = 0
icount = 0
jcount = 0

for i in range(9):
    for j in range(9):
        if num[i][j] > temp and num[i][j] != 0:
            temp = num[i][j]
            icount = i + 1
            jcount = j + 1

if icount == 0 and jcount == 0:
    icount += 1
    jcount += 1

print(temp)
print(icount, jcount)
