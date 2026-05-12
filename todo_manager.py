# todo_manager.py — a simple interactive to-do list

# Number of tasks and their descriptions
tasks = [1,2,3]
descriptions = ["Buy groceries", "Finish homework", "Call Dentist"]

print("=" * 30)
print("         To-Do List")
print("=" * 30)

print("1.",descriptions[0])
print("2.",descriptions[1])
print("3.",descriptions[2])

print("                 ")

print("Total tasks:", len(tasks))
task_number = len(tasks)

print("                 ")

print("What would you like to do?")
print("1. Add a task")
print("2. Remove a task")

print("                 ")
choice = input("Enter the number of your choice: ")
if choice == "1":
    new_task = input("Enter the description of the new task: ")
    tasks.append(len(tasks) + 1)
    descriptions.append(new_task)
    print("Task added successfully!")
elif choice == "2":
    task_number = int(input("Enter the number of the task to remove: "))
    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        descriptions.pop(task_number - 1)
        print("Task removed successfully!")
    else:
        print("Invalid task number.")   

print("Updated List:")
for i, description in enumerate(descriptions, start=1):
    print(f"{i}. {description}")

print("                 ")  

print("Total tasks:", len(tasks))

