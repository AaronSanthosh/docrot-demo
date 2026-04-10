"""In-memory storage helpers for tasks."""

from .models import Task


TASKS: dict[str, Task] = {}


def save_task(task: Task, *, overwrite: bool = True) -> dict[str, object]:
    """Store a task and return the saved task.

    If overwrite is False and the task already exists, raises ValueError.
    """

    if not overwrite and task.task_id in TASKS:
        raise ValueError(f"task {task.task_id} already exists")
    TASKS[task.task_id] = task
    return {"id": task.task_id, "stored": True}


def get_task(task_id: str) -> Task | None:
    """Return a task by its identifier."""

    return TASKS.get(task_id)


def remove_task(task_id: str) -> bool:
    """Delete a task by identifier and report success."""

    return TASKS.pop(task_id, None) is not None


def all_tasks(*, sort_by: str = "created_at") -> list[Task]:
    """Return every stored task as a sorted list."""

    tasks = list(TASKS.values())
    if sort_by == "priority":
        order = {"high": 0, "normal": 1, "low": 2}
        tasks.sort(key=lambda t: order.get(t.priority, 99))
    else:
        tasks.sort(key=lambda t: t.created_at)
    return tasks


def count_tasks() -> dict[str, int]:
    """Return a count of tasks grouped by status."""

    total = len(TASKS)
    completed = sum(1 for t in TASKS.values() if t.completed)
    archived = sum(1 for t in TASKS.values() if t.archived)
    return {"total": total, "completed": completed, "archived": archived, "active": total - completed - archived}


def clear_all() -> int:
    """Remove all tasks and return how many were deleted."""

    count = len(TASKS)
    TASKS.clear()
    return count
