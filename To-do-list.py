# Initialize an empty to-do list
todo_list = []

# Function to add a task
def add_task(task):
    todo_list.append(task)
    print("Task added: " + task)

# Function to list tasks
def list_tasks():
    if todo_list:
        print("To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")

# Function to mark a task as done
def mark_done(task_index):
    if 1 <= task_index <= len(todo_list):
        task = todo_list.pop(task_index - 1)
        print("Task marked as done: " + task)
    else:
        print("Invalid task index.")
        
#Function to remove task
def remove_task(task):
    todo_list.pop(task)
    print("Task removed: "- task)
    
# Main program loop
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Remove Task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        list_tasks()
        task_index = int(input("Enter the task number to remove: "))
        mark_done(task_index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
