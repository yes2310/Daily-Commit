def recursion(s, l, r):
    global count
    count += 1

    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)


n = int(input())
s = []

for i in range(n):
    s.append(input())

for j in range(n):
    count = 0
    print(isPalindrome(s[j]), count)
