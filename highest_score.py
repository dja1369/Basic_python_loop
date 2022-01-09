student_score = input("학생 들의 점수를 입력 하세요 : \n").split()
big = 0
for i in range (0 , len(student_score)):
    student_score[i] = int(student_score[i])
for n in student_score:
    if n > big:
        big = n
#최댓값 호출
print(max(student_score))
print(big)