from models.task import Task
from utils.validator import Validator
from services.file_service import FileService


class TaskService:
    """
    Manages task operations.
    """

    def __init__(self):
        self.__tasks = []
        self.load_tasks()

    def add_task(self, title, description, priority):

        try:
            Validator.validate_task_data(
                title,
                description,
                priority
            )

            task = Task(title, description, priority)

            self.__tasks.append(task)

            self.save_tasks()

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

            self.save_tasks()

            return "Task marked as completed."

        except IndexError:
            return "Invalid task index."

    def delete_task(self, index):

        try:
            deleted_task = self.__tasks.pop(index)

            self.save_tasks()

            return (
                f"Deleted task: "
                f"{deleted_task.get_title()}"
            )

        except IndexError:
            return "Invalid task index."

    def save_tasks(self):

        FileService.save_tasks(self.__tasks)

    def load_tasks(self):

        loaded_tasks = FileService.load_tasks()

        for task_data in loaded_tasks:

            task = Task(
                task_data["title"],
                task_data["description"],
                task_data["priority"]
            )

            if task_data["completed"]:
                task.mark_completed()

            self.__tasks.append(task)