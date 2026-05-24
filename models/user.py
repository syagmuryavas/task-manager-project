class User:
    """
    Represents a system user.
    """

    def __init__(self, username):
        self.__username = username

    def get_username(self):
        return self.__username

    def display_user_info(self):
        return f"Username: {self.__username}"