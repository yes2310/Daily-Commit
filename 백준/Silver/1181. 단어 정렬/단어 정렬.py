n = int(input())

word = []

for i in range(n):
    string = input()
    word.append([len(string), string])

word.sort(key=lambda x: (x[0], x[1]))

printedWord = []

for j in range(n):
    tempWord = word[j][1]

    if tempWord not in printedWord:
        print(tempWord)
        printedWord.append(tempWord)
