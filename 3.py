import numpy as np

# Project 3: Student Result Analyzer

# Q1. Find how many students passed.
# A student is considered PASS if marks are 40 or more (marks >= 40).

# Q2. Find how many students failed.
# A student is considered FAIL if marks are less than 40 (marks < 40).

# Q3. Find the average marks of only the passed students.
# Do not include failed students.

# Q4. Find the highest marks among only the passed students.

# Q5. Find the lowest marks among only the passed students.

# Q6. Find how many students scored higher than the overall class average.
# First find the average of all students, then count marks greater than that average.

# Q7. Print the marks of all students who scored higher than the overall class average.

# Q8. Check whether every student passed.
# Return True if every student's marks are 40 or more, otherwise return False.

# Q9. Check whether at least one student scored 90 or more.
# Return True if at least one student has marks >= 90, otherwise return False.

# Q10. Find the pass percentage.
# Pass percentage = (number of passed students / total number of students) × 100

def student_analyze(marks):
      pass_students=marks[marks>=40]
      fail_students=marks[marks<40]
      average=np.mean(pass_students)
      highest_marks=np.max(pass_students)
      lowest_marks=np.min(pass_students)
      student_average=np.mean(marks)
      count_student=np.sum(marks>student_average)
      pass_per=(pass_students/len(marks))*100

      all_pass=np.all(marks>=40)
      has_90=np.any(marks>=90)

      return pass_students,fail_students,average,highest_marks,lowest_marks,count_student,pass_per,all_pass,has_90
       
marks = np.array([35, 67, 82, 45, 91, 28, 74, 56, 39, 88])
pass_students,fail_students,average,highest_marks,lowest_marks,count_student,pass_per,all_pass,has_90=student_analyze(marks)
print(f"passed student is:{pass_students}\nfailed students is:{fail_students}\n average of passed students is:{average}\npassed highest students is :{highest_marks}\nlowest marks of passed student is:{lowest_marks}\nthe student how high than average is:{count_student}\npassed students percentage is:{pass_per}\n return true if student marks greater than 40 otherwise retuen false : {all_pass}\nreturn true if student marks atleast greater  than 90 otherwise retuen false : {has_90}")