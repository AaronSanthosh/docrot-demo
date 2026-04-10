"""Data models for the task manager."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import uuid4


@dataclass
class Task:
    """Represents a task with a title and optional notes."""

    title: str
    details: str = ""
    priority: str = "normal"
    completed: bool = False
    archived: bool = False
    tags: list[str] = field(default_factory=list)
    assignee: str | None = None
    due_date: Optional[datetime] = None
    task_id: str = field(default_factory=lambda: uuid4().hex[:8])
    created_at: datetime = field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None


def serialize_task(task: Task) -> tuple[str, dict[str, object]]:
    """Convert a task to a (id, data) tuple for structured output."""

    data = {
        "id": task.task_id,
        "title": task.title,
        "details": task.details,
        "priority": task.priority,
        "completed": task.completed,
        "archived": task.archived,
        "tags": list(task.tags),
        "assignee": task.assignee,
        "due_date": task.due_date.isoformat() + "Z" if task.due_date else None,
        "created_at": task.created_at.isoformat() + "Z",
        "completed_at": (
            task.completed_at.isoformat() + "Z" if task.completed_at else None
        ),
    }
    return (task.task_id, data)


def task_from_dict(data: dict[str, object], *, strict: bool = False) -> Task:
    """Reconstruct a Task from a serialized dictionary."""

    if strict and "title" not in data:
        raise ValueError("missing required field: title")

    return Task(
        title=str(data.get("title", "")),
        details=str(data.get("details", "")),
        priority=str(data.get("priority", "normal")),
        tags=list(data.get("tags", [])),
        assignee=data.get("assignee"),
    )
