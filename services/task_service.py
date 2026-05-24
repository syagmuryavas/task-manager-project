from models.task import Task
from utils.validator import Validator


class TaskService:
    """
    Manages task operations.
    """

    def __init__(self):
        self.__tasks = []

    def add_task(self, title, description, priority):

        try:
            Validator.validate_task_data(
                title,
                description,
                priority
            )

            task = Task(title, description, priority)

            self.__tasks.append(task)

            return "Task added successfully."

        except ValueError as error:
            return f"Error: {error}"

    def list_tasks(self):

        if not self.__tasks:
            return "No tasks available."

        task_list = []

        for index, task in enumerate(self.__tasks, start=1):
            task_info = (
                f"\nTask {index}\n"
                f"{task.display_task()}"
            )

            task_list.append(task_info)

        return "\n".join(task_list)

    def complete_task(self, index):

        try:
            self.__tasks[index].mark_completed()

            return "Task marked as completed."

        except IndexError:
            return "Invalid task index."

    def delete_task(self, index):

        try:
            deleted_task = self.__tasks.pop(index)

            return (
                f"Deleted task: "
                f"{deleted_task.get_title()}"
            )

        except IndexError:
            return "Invalid task index."