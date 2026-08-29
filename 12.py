#Project 12: Simple To-Do List

tasks = []

#Q1. Ask the user to enter 5 tasks and store them in the list.

for i in range(5):
    task=input("Enter your task:")
    tasks.append(task)
print(tasks)

#Q2.Display all the tasks with their task number.

for i in range(len(tasks)):
    print(i+1,tasks[i])

#Q3. Ask the user to enter a task number and delete that task from the list and then udpate than list

task_num=int(input("enter a task number  to delete :"))
tasks.pop(task_num-1)
print(f"after delete one task list is :{tasks}")

#Q4Ask the user to enter a new task and add it to the list and then  Display the final task list.

add_task=input("enter a new list yes/no:")
if add_task =="yes":
    user_add=input("enter a new task is :")
    tasks.append(user_add)

    print(f"the final task is :{tasks}")

else:
    print("no new task add")

#Q5.how many tasks are currently present in the list.

count_task=0
for i in tasks:
    count_task+=1

print(f"tasks are currently present in the list is {count_task}")    

#Q6 Check whether a particular task entered by the user is present in the list or not.

tell_user=input("enter a task :")
if tell_user in tasks:
    print("task is present in list")
else:
    print("not present in list")    
