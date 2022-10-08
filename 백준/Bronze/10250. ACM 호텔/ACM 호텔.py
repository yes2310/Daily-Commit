n = int(input())

hotel = []

for i in range(n):
    line = list(map(int, input().split()))
    hotel.append(line)

for j in range(n):
    if hotel[j][2] % hotel[j][0] == 0:
        print(hotel[j][0], end="")
    else:
        print(hotel[j][2] % hotel[j][0], end="")

    if -(-hotel[j][2] // hotel[j][0]) > 9:
        print(-(-hotel[j][2] // hotel[j][0]))
    else:
        print("0" + str(-(-hotel[j][2] // hotel[j][0])))
