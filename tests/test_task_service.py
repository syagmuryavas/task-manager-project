from services.task_service import TaskService
from services.file_service import FileService

def test_add_valid_task():

    service = TaskService()

    result = service.add_task(
        "Study Python",
        "Learn pytest",
        "High"
    )

    assert result == "Task added successfully."


def test_add_empty_title():

    service = TaskService()

    result = service.add_task(
        "",
        "Invalid task",
        "High"
    )

    assert "Error" in result


def test_add_invalid_priority():

    service = TaskService()

    result = service.add_task(
        "Task",
        "Description",
        "Very High"
    )

    assert "Error" in result


def test_complete_task():

    service = TaskService()

    service.add_task(
        "Complete homework",
        "Math exercises",
        "Medium"
    )

    result = service.complete_task(0)

    assert result == "Task marked as completed."


def test_complete_invalid_task():

    service = TaskService()

    result = service.complete_task(99)

    assert result == "Invalid task index."


def test_delete_task():

    service = TaskService()

    service.add_task(
        "Delete me",
        "Temporary task",
        "Low"
    )

    result = service.delete_task(0)

    assert "Deleted task" in result


def test_delete_invalid_task():

    service = TaskService()

    result = service.delete_task(100)

    assert result == "Invalid task index."


def test_list_empty_tasks():

    FileService.save_tasks([])

    service = TaskService()

    result = service.list_tasks()

    assert result == "No tasks available."


def test_list_tasks():

    service = TaskService()

    service.add_task(
        "Task 1",
        "Description 1",
        "High"
    )

    result = service.list_tasks()

    assert "Task 1" in result


def test_multiple_tasks():

    service = TaskService()

    service.add_task(
        "Task A",
        "Description A",
        "Low"
    )

    service.add_task(
        "Task B",
        "Description B",
        "Medium"
    )

    result = service.list_tasks()

    assert "Task A" in result
    assert "Task B" in result