"""Core task manager functions."""

from datetime import datetime

from .models import Task, serialize_task
from .storage import all_tasks, get_task, remove_task, save_task


def create_task(
    title: str,
    details: str = "",
    *,
    priority: str = "medium",
    tags: list[str] | None = None,
) -> dict[str, object]:
    """Create a task with a title and optional details."""

    cleaned_title = title.strip()
    if not cleaned_title:
        raise ValueError("title cannot be empty")

    task = Task(
        title=cleaned_title,
        details=details.strip(),
        priority=priority.lower(),
        tags=[tag.strip().lower() for tag in (tags or []) if tag.strip()],
    )
    save_task(task)
    return serialize_task(task)


def delete_task(task_id: str, *, archive: bool = False) -> dict[str, object]:
    """Delete a task by id and return whether it was removed."""

    task = get_task(task_id)
    if task is None:
        raise KeyError(f"unknown task: {task_id}")

    removed = remove_task(task_id)
    return {"deleted": removed, "archived": archive, "task_id": task_id}


def list_tasks(
    *,
    include_completed: bool = True,
    priority: str | None = None,
    tag: str | None = None,
) -> list[dict[str, object]]:
    """Return all current tasks."""

    items = all_tasks()
    if not include_completed:
        items = [task for task in items if not task.completed]
    if priority:
        items = [task for task in items if task.priority == priority.lower()]
    if tag:
        items = [task for task in items if tag.lower() in task.tags]
    return [serialize_task(task) for task in items]


def complete_task(task_id: str, *, completed_by: str = "system") -> dict[str, object]:
    """Mark a task as completed and return the updated task."""

    task = get_task(task_id)
    if task is None:
        raise KeyError(f"unknown task: {task_id}")

    task.completed = True
    task.completed_at = datetime.utcnow()
    payload = serialize_task(task)
    payload["completed_by"] = completed_by
    return payload


def rename_task(
    task_id: str, new_title: str, *, updated_by: str = "system"
) -> dict[str, object]:
    """Rename a task and return the updated record."""

    task = get_task(task_id)
    if task is None:
        raise KeyError(f"unknown task: {task_id}")

    if not new_title.strip():
        raise ValueError("new_title cannot be empty")

    task.title = new_title.strip()
    payload = serialize_task(task)
    payload["updated_by"] = updated_by
    return payload


def summarize_tasks() -> dict[str, int]:
    """Return a small summary of completion counts."""

    items = all_tasks()
    # Keep the summary compact for CLI-style output.
    completed = sum(1 for task in items if task.completed)

    return {
        "total": len(items),
        "completed": completed,
        "pending": len(items) - completed,
    }
