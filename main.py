from services.task_service import TaskService


def display_menu():

    print("\n===== TASK MANAGER SYSTEM =====")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def main():

    task_service = TaskService()

    while True:

        display_menu()

        choice = input("Select an option: ")

        if choice == "1":

            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input(
                "Enter priority (Low/Medium/High): "
            )

            result = task_service.add_task(
                title,
                description,
                priority
            )

            print(result)

        elif choice == "2":

            print(task_service.list_tasks())

        elif choice == "3":

            try:
                index = int(
                    input("Enter task index to complete: ")
                )

                result = task_service.complete_task(
                    index - 1
                )

                print(result)

            except ValueError:
                print("Invalid input.")

        elif choice == "4":

            try:
                index = int(
                    input("Enter task index to delete: ")
                )

                result = task_service.delete_task(
                    index - 1
                )

                print(result)

            except ValueError:
                print("Invalid input.")

        elif choice == "5":

            print("Exiting Task Manager System.")
            break

        else:
            print("Invalid menu option.")


if __name__ == "__main__":
    main()