import json

try:
    with open("tasks.json", "r") as file:
        tasks= json.load(file)
except FileNotFoundError:
    tasks= []

print("=== Student Task Tracker ===")
option =0

def add_task(tasks):
    title=input("Enter task title:")
    task={"title": title, "completed": False}
    tasks.append(task)
    autosave(tasks)
    print("Task added and saved!")

def view_tasks(tasks):
    if len(tasks) ==0:
        print("No tasks added yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            status="Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['title']} - {status}")

def mark_task_completed(tasks):
    if len(tasks)==0:
        print("No tasks to mark.")
    else:
        for i, task in enumerate(tasks, start=1):
            status="Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['title']} - {status}")

        task_number=int(input("Enter task number to mark as completed: "))
        if 1<= task_number <= len(tasks):
            tasks[task_number -1]["completed"]=True
            autosave(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

def delete_task(tasks):
    if len(tasks)==0:
        print("No tasks to delete.")
    else:
        for i, task in enumerate(tasks, start=1):
            status="Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['title']}- {status}")
        task_number= int(input("Enter task number to delete:"))
        if 1<=task_number <= len(tasks):
            confirm=input(f"Are you sure you want to delete '{tasks[task_number-1]['title']}? (y/n):").lower()
            if confirm=="y":
                deleted_task= tasks.pop(task_number -1)
                print(f"Deleted task: {deleted_task['title']}")
            else:
                print("Delete")
        else:
            print("Invalid task number.")

def autosave(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

while option !=5:
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")
    try: 
        option=int(input("Choose an option: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if option==1:
        add_task(tasks)
    elif option==2:
        view_tasks(tasks)
    elif option ==3:
        mark_task_completed(tasks)
    elif option ==4:
        delete_task(tasks)
    elif option ==5:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        print("Tasks saved.Goodbye!")
        
