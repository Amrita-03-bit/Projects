# Project 4: Student Attendance Analyzer

students = ["Aman", "Riya", "Neha", "Rahul", "Priya", "Karan"]
attendance = [92, 68, 81, 45, 76, 59]

# Q1. Find how many students have attendance of 75% or more.
# A student is considered eligible if attendance >= 75.
# Q2. Find how many students have attendance below 75%.

# Q3. Print the names of students who are eligible.
# Q4. Print the names of students who are NOT eligible.

def student_analyze(students, attendance):
  eligible_count=0
  not_eligible_count=0
  for i in range(len(students)):
        if attendance[i]>=75:
            eligible_count+=1
            print("eligible:",students[i])
        else:
            not_eligible_count+=1
            print("not eligible:",students[i])  
  return eligible_count, not_eligible_count
        
eligible_count, not_eligible_count = student_analyze(students, attendance)

print("Eligible count:", eligible_count)
print("Not eligible count:", not_eligible_count)        

# Q5. Find the student with the highest attendance.  
# # Print both the student's name and attendance percentage.  
#          
highest_attendance=attendance[0]       
high_index=0 

for index,value in enumerate(attendance):
        if value>highest_attendance:
            highest_attendance=value
            high_index=index
            
print("Highest attendance student:", students[high_index])
print("Attendance:", highest_attendance)

# Q6. Find the student with the lowest attendance.
# Print both the student's name and attendance percentage.

low_attendance=attendance[0]
low_index=0

for index,value in enumerate(attendance):
        if value<low_attendance:
            low_attedance=value
            low_index=index
            
print("Lowest attendance student:", students[low_index])
print("Attendance:", low_attendance) 

# Q7. Find the average attendance of the whole class.

count=0
average=0

for i in attendance:
    count+=i
average=count/len(attendance)
print(average)    

# Q8. Find how many students have attendance higher than the class average.

attendance_higher=0
for i in attendance:
    if i>average:
        attendance_higher+=1
print("Students above average:", attendance_higher)

# Q9. Create a function that takes students and attendance
# and returns the names of students whose attendance is 90% or more.

def high_attendance_students(students,attendance):
     result=[]
     for i in range(len(students)):
          if attendance[i]>=90:
               result.append(students[i])
     return result
print(high_attendance_students(students,attendance))  

# Q10. Create a function that gives a warning message:
# If attendance is below 50 → "Critical"
# If attendance is 50 to 74 → "Warning"
# If attendance is 75 or more → "Eligible"

def waring_measage(student,attendance):
     for i in attendance:
          if i<50:
               print("critical")
          elif i>=50 and i<75:
               print("warning")
          else:
               print("eligible")
waring_measage(students, attendance)               
                         

            

