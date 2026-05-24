import json


class FileService:
    """
    Handles file operations for task persistence.
    """

    FILE_PATH = "data/tasks.json"

    @staticmethod
    def save_tasks(tasks):

        task_data = []

        for task in tasks:
            task_info = {
                "title": task.get_title(),
                "description": task.get_description(),
                "priority": task.get_priority(),
                "completed": task.is_completed()
            }

            task_data.append(task_info)

        with open(
            FileService.FILE_PATH,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(task_data, file, indent=4)

    @staticmethod
    def load_tasks():

        try:
            with open(
                FileService.FILE_PATH,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            return []