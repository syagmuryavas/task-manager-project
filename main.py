from models.task import Task
from models.admin import Admin


task = Task(
    "Complete Project",
    "Finish the software configuration project",
    "High"
)

admin = Admin("yagmur")

print(task.display_task())
print()
print(admin.display_user_info())
print(admin.delete_task_message())