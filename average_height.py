student_height = input("학생 들의 키를 입력하세요 : \n").split()
average = 0
for i in range(0,len(student_height)):
    student_height[i] = int(student_height[i])
    average = int(average + student_height[i])
print(student_height)
average_calc = round(average/len(student_height))
print(f"학생들의 평균 키는 {average_calc} 입니다 .")