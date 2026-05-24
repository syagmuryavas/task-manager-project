from services.task_service import TaskService
from services.file_service import FileService


def test_complete_user_workflow():
    """
    System Test Scenario 1:
    User creates, completes and lists tasks.
    """

    FileService.save_tasks([])

    service = TaskService()

    add_result = service.add_task(
        "Prepare Presentation",
        "Prepare project presentation slides",
        "High"
    )

    assert add_result == "Task added successfully."

    complete_result = service.complete_task(0)

    assert complete_result == "Task marked as completed."

    task_list = service.list_tasks()

    assert "Completed" in task_list
    assert "Prepare Presentation" in task_list


def test_task_deletion_workflow():
    """
    System Test Scenario 2:
    User creates and deletes a task.
    """

    FileService.save_tasks([])

    service = TaskService()

    add_result = service.add_task(
        "Temporary Task",
        "This task will be removed",
        "Low"
    )

    assert add_result == "Task added successfully."

    delete_result = service.delete_task(0)

    assert "Deleted task" in delete_result

    task_list = service.list_tasks()

    assert task_list == "No tasks available."