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
    priority: str = "medium"
    completed: bool = False
    tags: list[str] = field(default_factory=list)
    task_id: str = field(default_factory=lambda: uuid4().hex[:8])
    created_at: datetime = field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None


def serialize_task(task: Task) -> dict[str, object]:
    """Convert a task to a printable dictionary."""

    return {
        "id": task.task_id,
        "title": task.title,
        "details": task.details,
        "priority": task.priority,
        "completed": task.completed,
        "tags": list(task.tags),
        "created_at": task.created_at.isoformat() + "Z",
        "completed_at": (
            task.completed_at.isoformat() + "Z" if task.completed_at else None
        ),
    }
