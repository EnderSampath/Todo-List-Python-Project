import os
import json

FILENAME = "todo_list.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    print("\nTo-Do List:")
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        print(f"{i+1}. {status} {task['name']}")
    print()

def add_task(tasks):
    name = input("Enter task name: ")
    tasks.append({"name": name, "done": False})
    print("Task added!")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        tasks[index]["done"] = True
        print("Task marked as done!")
    except:
        print("Invalid task number.")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        removed = tasks.pop(index)
        print(f"Removed task: {removed['name']}")
    except:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nOptions: [1] Show Tasks  [2] Add Task  [3] Mark Done  [4] Remove Task  [5] Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
