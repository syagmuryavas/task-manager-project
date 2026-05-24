from services.task_service import TaskService


task_service = TaskService()

print(task_service.add_task(
    "Complete Project",
    "Finish software configuration project",
    "High"
))

print(task_service.add_task(
    "",
    "Invalid task example",
    "High"
))

print(task_service.add_task(
    "Study Python",
    "Practice OOP concepts",
    "Medium"
))

print(task_service.list_tasks())

print(task_service.complete_task(0))

print(task_service.list_tasks())

print(task_service.delete_task(1))

print(task_service.list_tasks())