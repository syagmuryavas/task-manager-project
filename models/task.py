class Task:
    """
    Represents a task in the task management system.
    """

    def __init__(self, title, description, priority):
        self.__title = title
        self.__description = description
        self.__priority = priority
        self.__completed = False

    def mark_completed(self):
        self.__completed = True

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_priority(self):
        return self.__priority

    def is_completed(self):
        return self.__completed

    def update_task(self, title, description, priority):
        self.__title = title
        self.__description = description
        self.__priority = priority

    def display_task(self):
        status = "Completed" if self.__completed else "Pending"

        return (
            f"Title: {self.__title}\n"
            f"Description: {self.__description}\n"
            f"Priority: {self.__priority}\n"
            f"Status: {status}"
        )