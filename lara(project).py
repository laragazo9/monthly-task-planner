
tasks = []

# ------------------------- FUNCTIONS -------------------------

def show_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available!")
        return

    count = 1

    for task in tasks:
        if task["completed"] == True:
            print(count, "_", task["name"], "----> Completed")
        else:
            print(count, "_", task["name"], "----> Pending")

        count += 1


def delete_task(tasks):
    if len(tasks) == 0:
        print("No tasks available!")
        return

    show_tasks(tasks)

    try:
        ind = int(input("Enter task number to delete: ")) - 1

        if 0 <= ind < len(tasks):
            deleted = tasks.pop(ind)
            print(deleted["name"], "deleted successfully!")
        else:
            print("Task number is unavailable!")

    except ValueError:
        print("Enter numbers only please!")


def edit_task(tasks):
    if len(tasks) == 0:
        print("No tasks available!")
        return

    show_tasks(tasks)

    try:
        ind = int(input("Enter task number to edit: ")) - 1

        if 0 <= ind < len(tasks):
            new_name = input("Enter the new task name: ").strip()

            if new_name == "":
                print("Task name cannot be empty!")

            elif new_name.isdigit():
                print("Please enter a task name, not a number!")

            else:
                tasks[ind]["name"] = new_name
                print("Task updated successfully!")

        else:
            print("Task number is unavailable!")

    except ValueError:
        print("Enter numbers only please!")


def completed_task(tasks, ind):
    if tasks[ind]["completed"] == False:
        tasks[ind]["completed"] = True
        print("Task completed successfully!")
    else:
        print("The task is already completed!")


def count_completed(tasks):
    count = 0
    for i in tasks:
        if i["completed"] == True:
            count += 1
    return count


def count_pending(tasks):
    count = 0
    for i in tasks:
        if i["completed"] == False:
            count += 1
    return count


def count_total(tasks):
    count = 0
    for i in tasks:
        count += 1
    return count


# ------------------------- MAIN PROGRAM -------------------------

while True:
    print("=" * 35, "MONTHLY TASK PLANNER", "=" * 35)
    print("_" * 35, "ORGANIZE YOUR MONTH!", "_" * 35)

    print("1. Add Daily Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. View Monthly Report")
    print("5. Edit Task")
    print("6. Delete Task")
    print("7. Exit")

    # Validate menu choice
    try:
        your_choice = int(input("Enter Your Number Choice: "))
    except ValueError:
        print("Try again, number please!")
        continue

    # ------------------------- CHOICE 1 -------------------------

    if your_choice == 1:
        while True:
            your_task = input("Enter your daily task: ").strip()

            if your_task == "":
                print("Task name cannot be empty!")

            elif your_task.isdigit():
                print("Please enter a task name, not a number!")

            else:
                task = {
                    "name": your_task,
                    "completed": False
                }

                tasks.append(task)
                print("Task added successfully!")

            
            while True:
                choice = input(
                    "1. Add another task\n"
                    "2. Back to main menu\n"
                    "Select your choice: "
                ).strip().lower()

                if choice == "1" or choice == "add another task":
                    break

                elif choice == "2" or choice == "back to main menu":
                    break

                else:
                    print("Invalid choice! Please choose 1 or 2.")

            if choice == "2" or choice == "back to main menu":
                break

    # ------------------------- CHOICE 2 -------------------------

    elif your_choice == 2:
        show_tasks(tasks)

    # ------------------------- CHOICE 3 -------------------------

    elif your_choice == 3:
        if len(tasks) != 0:
            show_tasks(tasks)

            try:
                comp = int(input("Enter task number: "))
                ind = comp - 1

                if 0 <= ind < len(tasks):
                    completed_task(tasks, ind)
                else:
                    print("Task number is unavailable!")

            except ValueError:
                print("Enter numbers only please!")

        else:
            print("No tasks available!")

    # ------------------------- CHOICE 4 -------------------------

    elif your_choice == 4:
        print("Number of completed tasks =", count_completed(tasks))
        print("Number of pending tasks =", count_pending(tasks))
        print("Total tasks =", count_total(tasks))

    # ------------------------- CHOICE 5 -------------------------

    elif your_choice == 5:
        edit_task(tasks)

    # ------------------------- CHOICE 6 -------------------------

    elif your_choice == 6:
        delete_task(tasks)

    # ------------------------- CHOICE 7 -------------------------

    elif your_choice == 7:
        print("Logged out!")
        break

    else:
        print("Invalid choice! Please choose from 1 to 7.")
