s = input()
grade = 0.0

if s[0] == "A":
    grade = 4.0
elif s[0] == "B":
    grade = 3.0
elif s[0] == "C":
    grade = 2.0
elif s[0] == "D":
    grade = 1.0
else:
    grade = 0.0

if s[0] != "F":
    if s[1] == "+":
        grade += 0.3
    elif s[1] == "-":
        grade -= 0.3

print(grade)
