import numpy as np

expenses = np.array([120, 250, 80, 300, 150, 90, 450, 200, 175, 320])

'''1. Find the total expense.
2. Find the average expense.
3. Find the highest expense.
4. Find the lowest expense.
5. Count how many days had an expense greater than 200.
6. Print all expenses greater than 200.
7. Find the total of expenses less than 150.
8. Find the day/index with the highest expense.'''

total_expense=np.sum(expenses)
average_expense=np.mean(expenses)
highest_expense=np.max(expenses)
lowest_expense=np.min(expenses)
count_day=np.sum(expenses>200)
expense_greater_than_200=expenses[expenses>200]
total_expenses_less_than_150=np.sum(expenses[expenses<150])
highest_expenses_day=np.argmax(expenses)

print(f"total expenses is :{total_expense}\naverage expense is:{average_expense}\nhighest expense is:{highest_expense}\nlowest expenses is :{lowest_expense}\ntotal expenses day is :{count_day}\n greater than 200 expenses is:{expense_greater_than_200}\ntotal expenses less than 200 is :{total_expenses_less_than_150}\nhighest expenses day is :{highest_expenses_day}")

