def swap(n):
    temp = "000"

    temp = list(temp)
    n = list(n)

    temp[2] = n[0]
    temp[1] = n[1]
    temp[0] = n[2]

    return int(temp[0] + temp[1] + temp[2])


a, b = input().split()

a = swap(a)
b = swap(b)

print(max(a, b))
