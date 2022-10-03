input = list(input())

croatia = ["dz", "lj", "nj"]
count = 0

for i in range(len(input)):
    if input[i].isalpha():
        if input[i] == "d":
            try:
                if input[i + 1] == "z" and input[i + 2] == "=":
                    continue
            except IndexError:
                pass
        if input[i] == "l":
            try:
                if input[i + 1] == "j":
                    continue
            except IndexError:
                pass
        if input[i] == "n":
            try:
                if input[i + 1] == "j":
                    continue
            except IndexError:
                pass
        count += 1

print(count)
