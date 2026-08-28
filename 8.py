# Project 8: Student Marks Analyzer

students = ["Aman", "Riya", "Neha", "Rahul", "Priya", "Karan"]

marks = [85, 72, 45, 91, 63, 55]

subjects = ["Math", "Python", "English", "Science", "Computer", "Data"]

#Q1. Find the total marks of all students and also find the average marks of class

total_marks=0
for i in marks:
    total_marks+=i 
average=total_marks/len(marks)

print(f"total marks of all the students is :{total_marks}\naverage marks of the class:{average}")

#Q2. Find the student with the highest marks and lowest marks and  Print the student's name and marks.

high_marks=marks[0]
high_marks_student=students[0]
low_marks=marks[0]
low_marks_student=students[0]

for stu,mar in zip(students,marks):
    if mar>high_marks:
        high_marks=mar
        high_marks_student=stu
    if mar<low_marks:
        low_marks=mar
        low_marks_student=stu

print(f"highest marks students is :{high_marks_student} and marks is:{high_marks}\n lowest marks student is:{low_marks_student} and marks is :{low_marks}")        

#Q3. Find how many students scored 60 or more.

count_score=0
for i in marks:
    if i>=60:
        count_score+=1

print(f"student scored 60 or more than is :{count_score}")

#Q4. Print the names of students who scored 80 or more.

res=[]
for stu,mar in zip(students,marks):
    if mar>=80:
        res.append(stu)

print(f"names of students who scored 80 or more is :{res}")

#Q5. Create a list containing the names of students who scored between 50 and 79, inclusive.

res_1=[]
for stu,mar in zip(students,marks):
    if mar>=50 and mar<=79:
        res_1.append(stu)

print(f"names of students who scored between 50 and 79, inclusive is :{res_1}")

#Q6. Find how many students scored below the class average.

students_score=0
for stu,mar in zip(students,marks):
    if mar<average:
        students_score+=1

print(f"students scored below the class average is :{students_score}")

'''Q7. Give each student a performance status:
90 or more → Excellent
70–89 → Good
50–69 → Average
Below 50 → Poor'''

for stu,mar in zip(students,marks):
     if mar>=90:
         print(stu,"Excellent")
     elif mar>=70:
         print(stu,"Good")
     elif mar>=50:
         print(stu,"Average")
     else:
         print(stu,"Poor")            

#Q8. Create a list containing the names of students who passed A student passes if marks are 50 or more.

res_2=[]
for stu,mar in zip(students,marks):
    if mar>=50:
        res_2.append(stu)

print(f"students who passed A student passes if marks are 50 or more is :{res_2}")        

