
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        file.writelines(tasks)

def add_task():
    task = input("Enter the task: ")
    with open("tasks.txt", "a") as file:
        file.write("[ ] " + task + "\n")
    print("Task added!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

def mark_task_done():
    tasks = load_tasks()
    view_tasks()
    try:
        index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            if "[x]" in tasks[index]:
                print("Task is already marked as done.")
            else:
                tasks[index] = tasks[index].replace("[ ]", "[x]", 1)
                save_tasks(tasks)
                print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted: {removed.strip()}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n==== TO-DO LIST MENU ====")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
