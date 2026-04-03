# Architecture Overview

The project is organized as a few simple modules under `src/`.

## Modules

- `main.py` provides a small demo and directly calls the lower-level storage functions.
- `models.py` defines a `Task` object with `title`, `details`, and `completed` fields.
- `storage.py` stores tasks in a module-level list and exposes helper functions for CRUD operations.
- `task_manager.py` is a thin wrapper around storage and mostly forwards calls unchanged.

## Flow

1. `create_task(title, details="")` builds a task and returns only the new id.
2. `list_tasks()` reads from storage and returns task titles for display.
3. `mark_task_done(task_id)` flips the completion flag.
4. `delete_task(task_id)` removes the task silently if it exists.

## Notes

- The API does not raise exceptions for missing tasks; callers can rely on boolean return values.
- Tasks do not track priority, tags, timestamps, or completion metadata.
- Every public function in `task_manager.py` is documented in `API.md`.
