s = input().upper()

alpha = list(map(chr, (range(65, 91))))
sort = []

# 중복된 글자를 제외하여 리스트에 입력
for i in range(len(s)):
    if s[i] not in sort:
        sort.append(s[i])

count = list(0 for i in range(len(sort)))

# 중복을 제외한 글자를 이용하여 입력받았던 문자열에서 반복된 횟수를 세어 리스트에 입력
for j in range(len(sort)):
    count[j] = s.count(sort[j])

# count 함수를 이용했을 때 1을 넘은 값이 나오면 가장 많이 사용된 알파벳이 여러 개이므로 "?" 출력
# 그렇지 않은 경우엔 가장 많이 사용된 알파벳을 index 함수를 이용하여 출력
if count.count(max(count)) > 1:
    print("?")
else:
    print(sort[count.index(max(count))])
