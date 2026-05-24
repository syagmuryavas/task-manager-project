from services.task_service import TaskService
from services.file_service import FileService


def test_task_service_and_file_service():

    FileService.save_tasks([])

    service = TaskService()

    service.add_task(
        "Integration Task",
        "Testing services together",
        "High"
    )

    loaded_data = FileService.load_tasks()

    assert loaded_data[0]["title"] == "Integration Task"


def test_task_completion_and_persistence():

    FileService.save_tasks([])

    service = TaskService()

    service.add_task(
        "Complete Task",
        "Integration completion test",
        "Medium"
    )

    service.complete_task(0)

    loaded_data = FileService.load_tasks()

    assert loaded_data[0]["completed"] is True


def test_delete_task_and_file_update():

    FileService.save_tasks([])

    service = TaskService()

    service.add_task(
        "Temporary Task",
        "Will be deleted",
        "Low"
    )

    service.delete_task(0)

    loaded_data = FileService.load_tasks()

    assert loaded_data == []


def test_task_validation_integration():

    FileService.save_tasks([])

    service = TaskService()

    result = service.add_task(
        "",
        "Invalid integration task",
        "High"
    )

    assert "Error" in result


def test_multiple_module_integration():

    FileService.save_tasks([])

    service = TaskService()

    service.add_task(
        "Task A",
        "Description A",
        "Low"
    )

    service.add_task(
        "Task B",
        "Description B",
        "High"
    )

    loaded_data = FileService.load_tasks()

    assert len(loaded_data) == 2