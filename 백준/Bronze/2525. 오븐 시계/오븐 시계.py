h, m = map(int, input().split())
addTime = int(input())

addHour = (m + addTime) // 60
addMin = (m + addTime) % 60

if h + addHour < 24:
    print(h + addHour, addMin)
else:
    print(addHour - (24 - h), addMin)
