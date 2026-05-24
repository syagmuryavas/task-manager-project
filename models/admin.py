from models.user import User


class Admin(User):
    """
    Represents an admin user.
    """

    def __init__(self, username):
        super().__init__(username)

    def delete_task_message(self):
        return "Admin can delete tasks."