# API Reference

This project exposes a lightweight task manager API for creating and tracking todo items.

## `create_task(title, details="") -> str`

Creates a new task and returns the generated task id as a string.

Parameters:
- `title` (`str`): The task name.
- `details` (`str`): Optional description stored with the task.

## `delete_task(task_id) -> bool`

Deletes a task by id and returns `True` when the task existed.

Parameters:
- `task_id` (`str`): The id returned from `create_task`.

## `list_tasks() -> list[str]`

Returns a list containing the titles of all active tasks.

## `mark_task_done(task_id) -> bool`

Marks a task as done and returns `True` when successful.

Parameters:
- `task_id` (`str`): Identifier of the task to update.

## `save_task(task) -> Task`

Persists a task object in memory and returns the stored `Task`.

## `get_task(task_id) -> Task | None`

Looks up a task by id.

## `remove_task(task_id) -> bool`

Removes a task from storage.
