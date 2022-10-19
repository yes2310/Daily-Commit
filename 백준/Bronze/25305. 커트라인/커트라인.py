total, cut = map(int, input().split())

student = list(map(int, input().split()))

student.sort(reverse=True)

count = 0

for j in range(cut):
    count += 1

print(student[j])
