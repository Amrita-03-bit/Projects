#Project 10: Employee Salary Analyzer

employees = ["Aman", "Riya", "Neha", "Rahul", "Priya", "Karan"]

salaries = [25000, 42000, 18000, 55000, 32000, 65000]

#Q1. Find the total salary of all employees and also average

total_salary=0
for i in salaries:
    total_salary+=i
average=total_salary/len(salaries)    

print(f"total salary of employees is :{total_salary}\n average salary of employees is :{average}")

#Q3. Find the employee with the highest salary and lowest salary Print the employee's name and salary.'''

highest_salary=salaries[0]
lowest_salary=salaries[0]
high_salary_emp=employees[0]
low_salary_emp=employees[0]

for emp,sal in zip(employees,salaries):
    if sal>highest_salary:
        highest_salary=sal
        high_salary_emp=emp
    if sal<lowest_salary:
        lowest_salary=sal
        low_salary_emp=emp

print(f"highest salary employee is :{high_salary_emp} and salary is :{highest_salary}\n lowest salary employee is :{low_salary_emp} and salary is :{lowest_salary}")

#Q4. Find how many employees have a salary of ₹30,000 or more.

salary_count=0
for i in salaries:
    if i>=30000:
        salary_count+=1

print(f"employees have a salary of ₹30,000 or more is :{salary_count}")        

#Q5. Print the names of employees whose salary is ₹50,000 or more.

name_emp=[]
for emp,sal in zip(employees,salaries):
    if sal>=50000:
        name_emp.append(emp)

print(f"the names of employees whose salary is ₹50,000 or more is :{name_emp}")

#Q6. Create a list containing the names of employees whose salary is between ₹20,000 and ₹40,000, inclusive.

name_emp1=[]
for emp,sal in zip(employees,salaries):
    if sal>=20000 and sal<=40000:
        name_emp1.append(emp)

print(f"the names of employees whose salary is between ₹20,000 and ₹40,000, inclusive is :{name_emp1}")

#Q7. Find how many employees have a salary higher than the average salary.

salary_high=0
for i in salaries:
    if i>average:
        salary_high+=1

print(f"employees have a salary higher than the average salary is :{salary_high}")


'''Q9. Give each employee a salary category:
₹50,000 or more → "High Salary"
₹30,000–₹49,999 → "Medium Salary"
Below ₹30,000 → "Low Salary"'''

for emp,sal in zip(employees,salaries):
    if sal>=50000:
        print(emp,"High Salary")
    elif sal>=30000:
        print(emp,"Medium Salary")
    else:
        print(emp,"Low Salary")    

#Q10. Create a list containing the names of employees whose salary is below the average salary.

name_emp2=[]
for emp,sal in zip(employees,salaries):
    if sal<average:
        name_emp2.append(emp)

print(f"the names of employees whose salary is below the average salary is :{name_emp2}.")        
