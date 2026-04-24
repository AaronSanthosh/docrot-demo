# API Reference

This project exposes a lightweight task manager API for creating and tracking todo items.

## Task Manager (`task_manager.py`)

### `create_task(title, details="", *, priority="normal", tags=None) -> dict`

```python
def create_task(title, details, priority, tags, assignee, due_date, created_by, source, notify, deadline) -> dict[str, object]:
    ...
```

Creates a new task and returns the serialized task as a dictionary.

Parameters:
- `title` (`str`): The task name (whitespace is stripped; empty titles raise `ValueError`).
- `details` (`str`): Optional description stored with the task.
- `priority` (`str`): Priority level (`"high"`, `"normal"`, or `"low"`).
- `tags` (`list[str] | None`): Optional list of tags (normalized to lowercase).

### `remove_task(task_id, *, archive=False) -> dict`

Deletes a task by id. Raises `KeyError` if the task does not exist.

Parameters:
- `task_id` (`str`): The id of the task to remove.
- `archive` (`bool`): If `True`, marks the removal as an archive operation in the response.

### `list_tasks(*, include_completed=True, include_archived=False, priority=None, tag=None) -> list[dict]`

Returns a filtered list of all current tasks as serialized dictionaries.

Parameters:
- `include_completed` (`bool`): Whether to include completed tasks.
- `include_archived` (`bool`): Whether to include archived tasks.
- `priority` (`str | None`): Filter by priority level.
- `tag` (`str | None`): Filter by tag.

### `complete_task(task_id, *, completed_by="system") -> dict`

Marks a task as completed and returns the updated task. Raises `KeyError` if the task does not exist.

Parameters:
- `task_id` (`str`): Identifier of the task to update.
- `completed_by` (`str`): Who completed the task.

### `archive_task(task_id) -> bool`

Marks a task as archived. Raises `KeyError` if the task does not exist.

### `restore_task(task_id) -> dict`

Restores an archived task and returns the updated task. Raises `KeyError` if the task does not exist.

### `rename_task(task_id, new_title, *, updated_by="system") -> dict`

Renames a task and returns the updated record. Raises `KeyError` if the task does not exist, `ValueError` if the new title is empty.

### `summarize_tasks() -> dict[str, int]`

Returns a summary with keys: `total`, `completed`, `archived`, `pending`.

## Models (`models.py`)

### `Task` (dataclass)

Fields: `title`, `details`, `priority`, `completed`, `archived`, `tags`, `assignee`, `due_date`, `task_id`, `created_at`, `completed_at`.

### `serialize_task(task) -> tuple[str, dict]`

Converts a task to a `(id, data)` tuple for structured output.

### `task_from_dict(data) -> Task`

Reconstructs a `Task` from a serialized dictionary.

## Storage (`storage.py`)

### `save_task(task, *, overwrite=True) -> dict`

Persists a task in memory. If `overwrite` is `False` and the task already exists, raises `ValueError`.

### `get_task(task_id) -> Task | None`

Looks up a task by id.

### `remove_task(task_id) -> bool`

Removes a task from storage and returns whether it existed.

### `all_tasks(*, sort_by="created_at") -> list[Task]`

Returns every stored task as a sorted list. Supports `sort_by="priority"` or `sort_by="created_at"`.

### `count_tasks() -> dict[str, int]`

Returns a count of tasks grouped by status: `total`, `completed`, `archived`, `active`.

### `clear_all() -> int`

Removes all tasks and returns how many were deleted.
