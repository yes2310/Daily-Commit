n = input()

sum = 0

for i in range(len(n)):
    if n[i] == "A" or n[i] == "B" or n[i] == "C":
        sum += 3
    elif n[i] == "D" or n[i] == "E" or n[i] == "F":
        sum += 4
    elif n[i] == "G" or n[i] == "H" or n[i] == "I":
        sum += 5
    elif n[i] == "J" or n[i] == "K" or n[i] == "L":
        sum += 6
    elif n[i] == "M" or n[i] == "N" or n[i] == "O":
        sum += 7
    elif n[i] == "P" or n[i] == "Q" or n[i] == "R" or n[i] == "S":
        sum += 8
    elif n[i] == "T" or n[i] == "U" or n[i] == "V":
        sum += 9
    elif n[i] == "W" or n[i] == "X" or n[i] == "Y" or n[i] == "Z":
        sum += 10

print(sum)
