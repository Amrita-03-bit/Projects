#Project 6: Employee Performance Analyzer

employees = ["Aman", "Riya", "Neha", "Rahul", "Priya", "Karan"]
scores = [72, 91, 58, 84, 45, 96]

#Q1. Find how many employees scored 70 or more and also Find how many employees scored below 70.

total_employees_greater=0
total_employees=0
for i in scores:
    if i>=70:
        total_employees_greater+=1
    else:
        total_employees+=1    
print(f"total employees score greater than eqaul to 70 is: {total_employees_greater}\n total employees score smaller than eqaul to 70 is:{total_employees}  ")        

#Q2. Print the names of employees who scored 90 or more and also Print the names of employees who scored below 60
result=[]
result_1=[]
for employee,score in zip(employees,scores):
    if score>=90:
        result.append(employee)
    elif score<60:
        result_1.append(employee)
print(f"name of employees who score is greater than equai to 90 :{result}\n name of employees who score smaller than 60 is :{result_1}")            

#Q5. Find the employee with the highest score.Print the employee's name and score and also  Find the employee with the lowest score Print the employee's name and score.

highest_score=scores[0]
lowest_score=scores[0]
highest_employee=employees[0]
lowest_employee=employees[0]
for employee,score in zip(employees,scores):
    if score>highest_score:
        highest_score=score
        highest_employee=employee
    elif score<lowest_score:
        lowest_score=score
        lowest_employee=employee
print(f"highest score  employee is :{highest_employee} and score is :{highest_score}\n lowest score employee is :{lowest_employee} and score is :{lowest_score}")            

#Q7. Find the average score of all employees.

total_sum_employee=0
for i in scores:
    total_sum_employee+=i
average=total_sum_employee/len(scores)
print(f"average of all employees scores is : {average}")    

#Q8. Find how many employees scored higher than the average score.

scored_higher=0
total_scored_higher=0
for i in scores:
    if i>average:
        total_scored_higher+=1
print(f"total employees who scored higher than the average score:{total_scored_higher} ")        


#Q9. Create a list containing the names of employees whose score is between 60 and 89, inclusive.

name=[]

for score,employee in zip(scores,employees):
    if score<=89 and score>=60:
        score=employee
        name.append(employee)
print(f"employee scores between 60 to 89 is :{name}")        

'''Q10. Give each employee a performance status:

Score 90 or more → "Excellent"
Score 70–89 → "Good"
Score 50–69 → "Needs Improvement"
Score below 50 → "Poor"'''

for i in scores:
    if i>=90:
        print("Excellent")
    elif i>=70 and i<89:
        print("Good")
    elif i>=50:
        print("Need Improvement")
    else:
        print("Poor")            