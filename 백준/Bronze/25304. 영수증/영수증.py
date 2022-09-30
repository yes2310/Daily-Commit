sum = 0

total = int(input())
amount = int(input())

for i in range(amount):
    itemPrice, itemAmout = map(int, input().split())
    sum += itemPrice * itemAmout

if sum == total:
    print("Yes")
else:
    print("No")
