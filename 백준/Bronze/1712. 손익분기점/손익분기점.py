# 고정, 가변, 가격
A, B, C = map(int, input().split())

# 손익분기점
D = 0

try:
    D = int(A / (C - B) + 1)
except ZeroDivisionError:
    pass

# 출력
if D < 1:
    print(-1)
else:
    print(D)
