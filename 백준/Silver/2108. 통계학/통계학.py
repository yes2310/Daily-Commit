import sys


def mode(numList):
    count = {}
    maxList = []

    for i in numList:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    countMax = max(count.values())

    for j in count:
        if countMax == count[j]:
            maxList.append(j)

    if len(maxList) > 1:
        print(maxList[1])
    else:
        print(maxList[0])


numList = []

for i in range(int(sys.stdin.readline())):
    numList.append(int(sys.stdin.readline()))

numList.sort()

arithmeticMean = round(sum(numList) / len(numList))

median = numList[len(numList) // 2]

rangeNum = max(numList) - min(numList)


print(arithmeticMean)
print(median)
mode(numList)
print(rangeNum)
