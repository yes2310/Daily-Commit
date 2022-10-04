n = int(input())

if n == 1:
    print(1)
else:
    i = 1
    temp = 1

    while True:
        if n <= temp + 6 * i:
            print(i + 1)
            break
        else:
            temp += 6 * i
            i += 1
