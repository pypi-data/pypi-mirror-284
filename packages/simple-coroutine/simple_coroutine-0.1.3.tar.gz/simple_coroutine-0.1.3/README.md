# CoroutineSession

`CoroutineSession` is a designed to manage and execute asyncio tasks with optional progress tracking and callbacks. It supports running tasks with a concurrency limit and batching delay.

## Features

- Add and manage asyncio tasks.
- Execute tasks with a specified maximum number of concurrent tasks.
- Delay between batches of tasks for better control over execution.
- Optional callback functions to handle task completion and progress updates.
- Progress tracking with individual task shares for better granularity.

## Installation

This class is part of a Python project and requires Python 3.7 or later. Ensure you have `pydantic` installed:

```bash
pip install simple-coroutine
```

```python
import asyncio
from simple_coroutine.manager import CoroutineSession

async def sample_task(task_id):
    await asyncio.sleep(2)  # Simulate a task taking some time
    return f"Task {task_id} completed"

async def main():
    session = CoroutineSession(
        max_concurrent_tasks=2,
        batch_delay=5,
        callback=lambda index, result: print(f"Task {index} result: {result}"),
        progress_callback=lambda index, progress, total: print(f"Task {index} progress: {progress}, Total: {total}")
    )

    tasks = [sample_task(i) for i in range(5)]
    session.add_task_set(tasks)
    
    results = await session.run_tasks()
    print("All tasks completed:", results)

    async for progress in session.progress_generator():
        print(f"Progress: {progress}%")

if __name__ == "__main__":
    asyncio.run(main())
```