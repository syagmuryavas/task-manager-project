class Validator:
    """
    Provides validation methods for task data.
    """

    @staticmethod
    def validate_task_data(title, description, priority):

        if not title.strip():
            raise ValueError("Task title cannot be empty.")

        if not description.strip():
            raise ValueError("Task description cannot be empty.")

        valid_priorities = ["Low", "Medium", "High"]

        if priority not in valid_priorities:
            raise ValueError(
                "Priority must be Low, Medium, or High."
            )

        return True