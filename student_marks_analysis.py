import numpy as np
Student_marks = np.array([65,77,85,45,35,90,95,80,86,54,60,99])
avg_marks = Student_marks.mean()
print(np.round(avg_marks, 2))
highest_marks = Student_marks.max()
print(highest_marks)
lowest_marks = Student_marks.min()
print(lowest_marks)
passed_students = Student_marks[Student_marks > 40]
print(passed_students)
print(passed_students.size)
failed_students = Student_marks[Student_marks < 40]
print(failed_students)
print(failed_students.size)
above_75 = Student_marks[Student_marks > 75]
print(above_75)
grace_marks = Student_marks + 5
print(grace_marks)
total_marks = Student_marks.sum()
print(total_marks)
btw_60_80 = Student_marks[(Student_marks > 60) & (Student_marks < 80)]
print(btw_60_80)
print(Student_marks.size)
percent_pass = (passed_students.size/Student_marks.size) * 100
print(np.round(percent_pass, 2),"%")
