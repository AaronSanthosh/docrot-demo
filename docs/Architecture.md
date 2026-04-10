# Architecture Overview

The project is organized as a few simple modules under `src/`.

## Modules

- `main.py` provides a demo entrypoint with `bootstrap_demo(verbose=False)` that creates sample tasks and `run_full_lifecycle()` that demonstrates the full create/rename/complete/archive/restore flow.
- `models.py` defines a `Task` dataclass with `title`, `details`, `priority`, `completed`, `archived`, `tags`, `assignee`, `due_date`, and timestamp fields. Also provides `serialize_task` (returns a tuple) and `task_from_dict` for deserialization.
- `storage.py` stores tasks in a module-level dictionary and exposes helpers: `save_task` (with overwrite control), `get_task`, `remove_task`, `all_tasks` (with sorting), `count_tasks`, and `clear_all`.
- `task_manager.py` provides the public API layer with full CRUD operations: `create_task`, `remove_task`, `list_tasks` (with filtering), `complete_task`, `archive_task`, `restore_task`, `rename_task`, and `summarize_tasks`.

## Flow

1. `create_task(title, details, priority, tags)` builds a task, saves it, and returns a serialized dict.
2. `list_tasks(include_completed, include_archived, priority, tag)` reads from storage with filtering and returns serialized tasks.
3. `complete_task(task_id, completed_by)` marks the task done and records the timestamp.
4. `remove_task(task_id, archive)` deletes the task and raises `KeyError` if not found.
5. `archive_task` / `restore_task` toggle the archived state.
6. `rename_task(task_id, new_title)` updates the task title.

## Notes

- The API raises `KeyError` for missing tasks and `ValueError` for invalid input (empty titles, duplicate saves).
- Tasks track priority, tags, assignee, due dates, and completion metadata.
- `storage.py` supports sorting by creation time or priority, and provides `count_tasks` for status summaries.
- Every public function in `task_manager.py` is documented in `API.md`.
