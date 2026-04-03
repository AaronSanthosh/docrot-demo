"""Example command-line entrypoint for the task manager."""

from .task_manager import complete_task, create_task, list_tasks, summarize_tasks


def bootstrap_demo() -> dict[str, object]:
    """Populate a small demo dataset and return a summary."""

    first = create_task("Write outline", "Draft the release outline", priority="high")
    second = create_task(
        "Review docs",
        "Compare API docs with implementation",
        tags=["docs", "cleanup"],
    )
    complete_task(first["id"], completed_by="demo-user")
    return {
        "created_ids": [first["id"], second["id"]],
        "visible_tasks": list_tasks(include_completed=True),
        "summary": summarize_tasks(),
    }


if __name__ == "__main__":
    print(bootstrap_demo())
