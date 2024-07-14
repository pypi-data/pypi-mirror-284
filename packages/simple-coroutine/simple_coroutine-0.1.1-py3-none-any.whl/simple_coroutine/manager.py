from pydantic import BaseModel, PrivateAttr
import asyncio
from typing import Optional, Callable, Any, List, Tuple, AsyncGenerator

class CoroutineSession(BaseModel):
    """
    A class to manage and run asyncio tasks with optional progress tracking and callbacks.

    Attributes:
        tasks (List): List of asyncio tasks to be executed.
        max_concurrent_tasks (int): Maximum number of concurrent tasks (0 means no limit).
        batch_delay (int): Delay between batches of tasks when max_concurrent_tasks > 0.
        callback (Optional[Callable[[int, Any], None]]): Optional callback function to be called with task index and result.
        progress_callback (Optional[Callable[[int, float, float], None]]): Optional callback for progress tracking, including task index, individual progress, and total progress.
        task_shares (Optional[List[int]]): Optional list of shares for each task to indicate their weight in the total progress.
        progress_log (List[Tuple[int, float]]): Log of progress updates.
        total_progress (int): Total progress made across all tasks.
    """
    
    tasks: List = []
    max_concurrent_tasks: int = 0  # 0 means no limit
    batch_delay: int = 60
    callback: Optional[Callable[[int, Any], None]] = None
    progress_callback: Optional[Callable[[int, float, float], None]] = None  # Updated to include total progress
    task_shares: Optional[List[int]] = None
    progress_log: List[Tuple[int, float]] = []
    total_progress: int = 0
    _progress_queue: asyncio.Queue = PrivateAttr(default_factory=asyncio.Queue)

    def add_task(self, coro):
        """
        Add a single asyncio task to the session.

        Args:
            coro (coroutine): The asyncio task to be added.
        """
        self.tasks.append(coro)
    
    def add_task_set(self, coros):
        """
        Add a set of asyncio tasks to the session.

        Args:
            coros (list): List of asyncio tasks to be added.
        """
        self.tasks.extend(coros)
    
    def clear_tasks(self):
        """
        Clear all tasks from the session.
        """
        self.tasks = []

    def calculate_shares(self):
        """
        Calculate the share of total progress for each task.
        """
        if self.task_shares is None:
            num_tasks = len(self.tasks)
            share = int(100 / num_tasks)
            self.task_shares = [share] * num_tasks
            remainder = 100 - sum(self.task_shares)
            for i in range(int(remainder)):
                self.task_shares[i] += 1

    async def run_tasks(self):
        """
        Run all tasks in the session with optional concurrency limit and batch delay.

        Returns:
            List: Results of the executed tasks.
        """
        self.calculate_shares()

        async def run_task_with_callback(coro, index, share):
            try:
                if self.progress_callback:
                    self.progress_callback(index, share / 2, self.total_progress)
                    self.progress_log.append((index, share / 2))
                await self._progress_queue.put(self.total_progress)

                result = await coro
            except Exception as e:
                result = e
            if self.callback:
                if asyncio.iscoroutinefunction(self.callback):
                    await self.callback(index, result)
                else:
                    self.callback(index, result)
            if self.progress_callback:
                self.total_progress += share
                self.progress_callback(index, share / 2, self.total_progress)
                self.progress_log.append((index, share / 2))
            await self._progress_queue.put(self.total_progress)
            return result

        if self.tasks:
            if self.max_concurrent_tasks > 0:
                semaphore = asyncio.Semaphore(self.max_concurrent_tasks)
                results = []
                for i in range(0, len(self.tasks), self.max_concurrent_tasks):
                    batch = self.tasks[i:i+self.max_concurrent_tasks]
                    async with semaphore:
                        batch_results = await asyncio.gather(
                            *(run_task_with_callback(task, i+j, self.task_shares[i+j]) for j, task in enumerate(batch))
                        )
                        results.extend(batch_results)
                    await asyncio.sleep(self.batch_delay)
                self.tasks.clear()
                return results
            else:
                results = await asyncio.gather(
                    *(run_task_with_callback(task, i, self.task_shares[i]) for i, task in enumerate(self.tasks))
                )
                self.tasks.clear()
                return results

    async def progress_generator(self) -> AsyncGenerator[float, None]:
        """
        Generate progress updates.

        Yields:
            float: Current progress percentage.
        """
        while True:
            progress = await self._progress_queue.get()
            yield progress
            if progress >= 100:
                break
