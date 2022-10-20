numList = []

num = input()

for i in num:
    numList.append(int(i))

numList.sort(reverse=True)

for j in range(len(numList)):
    print(numList[j], end="")
