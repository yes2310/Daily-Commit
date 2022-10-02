s = input()

alpha = list(map(chr, (range(97, 123))))
output = list(-1 for i in range(len(alpha)))

for i in range(len(s)):
    if output[alpha.index(s[i])] == -1:
        output[alpha.index(s[i])] = i

for i in range(len(output)):
    print(output[i], end=" ")
