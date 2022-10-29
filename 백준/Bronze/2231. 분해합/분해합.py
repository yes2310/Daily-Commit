n = int(input())

for i in range(n):
    strNum = str(i)
    lenNum = len(strNum)
    temp = i

    for j in range(lenNum):
        temp += int(strNum[j])

    if temp == n:
        print(i)
        exit(0)

print(0)
