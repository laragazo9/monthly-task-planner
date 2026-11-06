
tasks = []

# ------------------------- FUNCTIONS -------------------------

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
    print("5. Exit")

    # Validate menu choice
    try:
        your_choice = int(input("Enter Your Number Choice: "))
    except ValueError:
        print("Try again, number please!")
        continue

    # ------------------------- CHOICE 1 -------------------------

    if your_choice == 1:
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

    # ------------------------- CHOICE 2 -------------------------

    elif your_choice == 2:
        if len(tasks) != 0:
            for i in tasks:
                if i["completed"] == True:
                    print(i["name"], " ----> Completed")
                else:
                    print(i["name"], "---->Pending")
        else:
            print("No tasks available!")

    # ------------------------- CHOICE 3 -------------------------

    elif your_choice == 3:
        try:
            comp = int(input("Enter task number: "))
            ind = comp - 1

            if len(tasks) > ind and ind >= 0:
                completed_task(tasks, ind)
            else:
                print("Task number is unavailable!")

        except ValueError:
            print("Enter numbers only please!")

    # ------------------------- CHOICE 4 -------------------------

    elif your_choice == 4:
        print("Number of completed tasks =", count_completed(tasks))
        print("Number of pending tasks =", count_pending(tasks))
        print("Total tasks =", count_total(tasks))

    # ------------------------- CHOICE 5 -------------------------

    elif your_choice == 5:
        print("Logged out!")
        break

    else:
        print("Invalid choice! Please choose from 1 to 5.")
