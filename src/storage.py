"""In-memory storage helpers for tasks."""

from collections.abc import Iterable

from .models import Task


TASKS: dict[str, Task] = {}


def save_task(task: Task) -> dict[str, object]:
    """Store a task and return the saved task."""

    TASKS[task.task_id] = task
    return {"id": task.task_id, "stored": True}


def get_task(task_id: str) -> Task | None:
    """Return a task by its identifier."""

    return TASKS.get(task_id)


def remove_task(task_id: str) -> bool:
    """Delete a task by identifier and report success."""

    return TASKS.pop(task_id, None) is not None


def all_tasks() -> list[Task]:
    """Return every stored task as a list."""

    return list(TASKS.values())


def load_seed_tasks(tasks: Iterable[Task]) -> int:
    """Bulk-load initial tasks and return the amount inserted."""

    count = 0
    for task in tasks:
        TASKS[task.task_id] = task
        count += 1
    return count
