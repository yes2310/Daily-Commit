count = 0
dice = list(map(int, input().split()))
max = max(dice)


for i in dice:
    if dice.count(i) > count:
        count = dice.count(i)
        same = i

if dice[0] == dice[1] == dice[2]:
    print(10000 + dice[0] * 1000)
elif count == 2:
    print(1000 + same * 100)
elif dice[0] != dice[1] != dice[2]:
    print(max * 100)
