n = int(input())

i = 0
sum = 0

up = 1
down = 1

if n != 1:
    while sum < n:
        i += 1
        sum += i

    # 분자 or 분모로 시작할 start 변수
    start = i

    # 총 몇번 분수를 찾는지를 저장하는 result변수
    result = n - (sum - i)

    if i % 2 != 0:
        up = start

        for j in range(1, result):
            up -= 1
            down += 1
    else:
        down = start

        for k in range(1, result):
            up += 1
            down -= 1

print(str(up) + "/" + str(down))
