import numpy as np

# Project 1: Student Marks Analyzer

marks = np.array([78, 65, 92, 55, 88, 71, 45, 95])

# Task:
# 1. Find the average marks.
# 2. Find the highest marks.
# 3. Find the lowest marks.
# 4. Count the number of students who scored more than 50 marks.
# 5. Print the marks that are greater than 80.

average_marks=np.mean(marks)
highest_marks=np.max(marks)
lowest_marks=np.min(marks)
count=np.sum(marks>50)
eighty_plus=marks[marks>80]
            

print(f"average marks is :{average_marks}\nhighest marks is :{highest_marks}\nlowest marks is :{lowest_marks}\n total 50 plus student :{count}\n 80 plus student:{eighty_plus}")