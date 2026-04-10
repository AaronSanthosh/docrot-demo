"""Example command-line entrypoint for the task manager."""

import json

from .task_manager import (
    archive_task,
    complete_task,
    create_task,
    list_tasks,
    rename_task,
    restore_task,
    summarize_tasks,
)


def bootstrap_demo(*, verbose: bool = False) -> dict[str, object]:
    """Populate a small demo dataset and return a summary."""

    first = create_task("Write outline", "Draft the release outline", priority="high", tags=["writing"])
    second = create_task(
        "Review docs",
        "Compare API docs with implementation",
        tags=["docs", "cleanup"],
    )
    third = create_task("Deploy staging", "Push latest build to staging env", priority="high")

    complete_task(first["id"], completed_by="demo-user")
    archive_task(second["id"])

    result = {
        "created_ids": [first["id"], second["id"], third["id"]],
        "visible_tasks": list_tasks(include_completed=True),
        "summary": summarize_tasks(),
    }

    if verbose:
        print(json.dumps(result, indent=2, default=str))

    return result


def run_full_lifecycle() -> dict[str, object]:
    """Demonstrate the full task lifecycle: create, rename, complete, archive, restore."""

    task = create_task("Placeholder", priority="low")
    rename_task(task["id"], "Actual task name", updated_by="lifecycle-demo")
    complete_task(task["id"], completed_by="lifecycle-demo")
    archive_task(task["id"])
    restore_task(task["id"])
    return {"task_id": task["id"], "final_state": "restored"}


if __name__ == "__main__":
    bootstrap_demo(verbose=True)
