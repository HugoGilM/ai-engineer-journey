"""Exercise 3: 20 jobs, at most 5 at once, whole batch limited to 4 seconds."""

import asyncio
import random
import time

MAX_CONCURRENT = 5
BATCH_TIMEOUT_SECS = 4.0
JOBS = 20


async def work(name: str, secs: float) -> str:
    """Sleep without blocking the loop, then return the name."""
    await asyncio.sleep(secs)
    return name


async def limited(sem: asyncio.Semaphore, name: str, secs: float) -> str:
    """Wait for a free slot (like SemaphoreSlim.WaitAsync), then do the work."""
    async with sem:
        return await work(name, secs)


async def main() -> None:
    """Run the batch and report how many jobs finished before the deadline."""
    sem = asyncio.Semaphore(MAX_CONCURRENT)
    durations = [random.uniform(0.5, 2.0) for _ in range(JOBS)]
    print(
        f"total work {sum(durations):.1f}s / {MAX_CONCURRENT} slots "
        f"= ~{sum(durations) / MAX_CONCURRENT:.1f}s ideal"
    )

    tasks: list[asyncio.Task[str]] = []
    start = time.perf_counter()
    try:
        async with asyncio.timeout(BATCH_TIMEOUT_SECS):
            async with asyncio.TaskGroup() as tg:
                for i, secs in enumerate(durations):
                    tasks.append(tg.create_task(limited(sem, f"job{i}", secs)))
        print("all jobs finished in time")
    except TimeoutError:
        print(f"timed out after {BATCH_TIMEOUT_SECS}s")

    finished = sum(1 for t in tasks if t.done() and not t.cancelled())
    print(f"{finished}/{JOBS} finished in {time.perf_counter() - start:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
