# Collection to store tasks
tasks = []

# Procedure to add a task
def add_task(task_list, task_name):
    """Adds a task to the task list if it doesn't already exist."""
    if task_name not in task_list:
        task_list.append({"name": task_name, "completed": False})
        print(f"Task '{task_name}' added.")
    else:
        print(f"Task '{task_name}' already exists.")

# Procedure to mark a task as completed
def complete_task(task_list, task_name):
    """Marks a task as completed if it exists."""
    found = False
    for task in task_list:
        if task["name"] == task_name:
            task["completed"] = True
            print(f"Task '{task_name}' marked as completed.")
            found = True
            break
    if not found:
        print(f"Task '{task_name}' not found.")

# Procedure to display all tasks
def display_tasks(task_list):
    """Displays all tasks with their status."""
    if not task_list:
        print("No tasks available.")
    else:
        for task in task_list:
            status = "Done" if task["completed"] else "Pending"
            print(f"- {task['name']} [{status}]")

# Main program loop
def main():
    while True:
        print("\nOptions: 1. Add Task  2. Complete Task  3. Show Tasks  4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task_name = input("Enter task name: ")
            add_task(tasks, task_name)  # Call to procedure
        elif choice == "2":
            task_name = input("Enter task name to mark as complete: ")
            complete_task(tasks, task_name)  # Call to procedure
        elif choice == "3":
            display_tasks(tasks)  # Call to procedure
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function to start the program
main()
