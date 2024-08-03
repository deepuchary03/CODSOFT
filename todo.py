import os
def see_tasks(file):
    try:
        with open(file, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []
def save_tasks(file, task):
    with open(file, 'w') as file:
        file.writelines(task)
def add_task(tasks, task):
    tasks.append(task)
    tasks.append("\n")
    return tasks   
#we can assume tn as no of tasks
def delete_task(tasks, tn):
    try:
        del tasks[tn- 1]
        return tasks
    except IndexError:
        print("Invalid task number.")
        return tasks
def update_task(tasks, tn, new_task):
    try:
        tasks[tn - 1] = new_task + "\n"
        return tasks
    except IndexError:
        print("Invalid task number.")
        return tasks
def display_tasks(tasks):
    print("To-Do List:")
    i = 1
    for task in tasks:
        print(str(i) + ". " + task.strip())
        i += 1
def main():
    file = "TODOLlist.txt"
    tasks = see_tasks(file)

    while True:
        print("--TODO LIST--")
        print("1. Add tasks")
        print("2. Delete tasks")
        print("3. Update task")
        print("4. Display tasks")
        print("5. Exit")
        print("Enter your choice:")
        ch = input()

        if ch == "1":
            task = input("Enter task: ")
            tasks = add_task(tasks, task)
            save_tasks(file, tasks)
        elif ch == "2":
            task_number = int(input("Enter task number to delete: "))
            tasks = delete_task(tasks, task_number)
            save_tasks(file, tasks)
        elif ch == "3":
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            tasks = update_task(tasks, task_number, new_task)
            save_tasks(file, tasks)
        elif ch == "4":
            display_tasks(tasks)
        elif ch == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
