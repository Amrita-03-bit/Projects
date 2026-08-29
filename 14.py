#Project 14: Student Result Management System

students={}

#Q1.Create a function to add a student
def add_student():

    stu_name=input("Enter student name:")
    stu_roll=int(input("Enter student rollno :"))

    stu_marks=[] 
    for i in range(3):
        marks=int(input("enter student marks:"))
        stu_marks.append(marks)

    students[stu_roll] = {
    "name": stu_name,
    "marks": stu_marks
    }
add_student()
print(students)

#Q2.Calculate the student's total marks ,percentage and grade check student pass fail
    
def student_marks_information():

    roll_num=int(input("enter a student roll no :"))

    if roll_num in students:
      marks=students[roll_num]["marks"]

      total_marks=0
      for i in marks:
        total_marks+=i
      print(total_marks)
      

      percentage=(total_marks/300)*100
      print("percentage :",percentage)
      
               
      if percentage >= 90:
         print("Grade A")
      
      elif percentage >= 75:
          print("Grade B")
      
      elif percentage>= 60:
          print("Grade C")
      
      elif percentage >= 40:
          print("Grade D")
      
      else:
          print("Grade F")

      if total_marks>=40:
         print(" student PASS")    

      else:
         print("student FAIL")   
    else:
       print("student roll no not found")
student_marks_information()  





