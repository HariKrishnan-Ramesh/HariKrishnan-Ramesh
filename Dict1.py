student_marks = {
    "Jenny" : 92,
    "Harry" : 78,
    "Dimpy" : 56,
    "Rahul" : 41,
    "Aniket": 99,
    "Prem"  : 34,
}

student_grades={}
for i in student_marks:
    marks=student_marks[i]
    if marks>90 and marks<=100:
        student_grades[i]='A+'
    elif marks>80 and marks<=90:
        student_grades[i]='A'
    elif marks>70 and marks<=80:
        student_grades[i]='B+'
    elif marks>60 and marks<=70:
        student_grades[i]='B'
    elif marks>50 and marks<=60:
        student_grades[i]='C'
    elif marks>40 and marks<=50:
        student_grades[i]='D'
    elif marks<40:
        student_grades[i]='fail'
    else:
        print("Error")

print(student_marks)
print(student_grades)