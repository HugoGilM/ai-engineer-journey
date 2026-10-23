"""Exercise 1: feel the event loop — sequential vs gather vs TaskGroup."""

import asyncio
import time
from collections.abc import Awaitable, Callable


async def work(name: str, secs: float) -> str:
    """Sleep without blocking the loop, then return the name."""
    await asyncio.sleep(secs)  # like await Task.Delay(...)
    return name


async def blocking_work(name: str, secs: float) -> str:
    """Same as work, but time.sleep blocks the whole thread (like Thread.Sleep)."""
    time.sleep(secs)  # noqa: ASYNC251 — blocking on purpose for the lesson
    return name


async def sequential() -> list[str]:
    """Await one after another. Prediction: 1 + 2 + 3 = ~6s."""
    a = await work("a", 1)
    b = await work("b", 2)
    c = await work("c", 3)
    return [a, b, c]


async def with_gather() -> list[str]:
    """Run concurrently, like Task.WhenAll. Prediction: max(1, 2, 3) = ~3s."""
    return list(await asyncio.gather(work("a", 1), work("b", 2), work("c", 3)))


async def with_taskgroup() -> list[str]:
    """Run concurrently with structured cancellation. Prediction: ~3s."""
    async with asyncio.TaskGroup() as tg:
        ta = tg.create_task(work("a", 1))
        tb = tg.create_task(work("b", 2))
        tc = tg.create_task(work("c", 3))
    # Leaving the block waits for every task; if one fails the rest are cancelled.
    return [ta.result(), tb.result(), tc.result()]


async def with_gather_blocking() -> list[str]:
    """Gather over blocking calls. Prediction: ~6s — no concurrency at all."""
    results = await asyncio.gather(
        blocking_work("a", 1), blocking_work("b", 2), blocking_work("c", 3)
    )
    return list(results)


async def timed(label: str, coro_fn: Callable[[], Awaitable[list[str]]]) -> None:
    """Run a zero-arg coroutine function and print how long it took."""
    start = time.perf_counter()
    results = await coro_fn()
    print(f"{label:<18} {results}  {time.perf_counter() - start:.2f}s")


async def main() -> None:
    """Time the four variants."""
    await timed("sequential", sequential)
    await timed("gather", with_gather)
    await timed("taskgroup", with_taskgroup)
    await timed("gather+time.sleep", with_gather_blocking)
    # Why ~6s: time.sleep never yields to the event loop. The loop is single-threaded,
    # so while one coroutine sleeps nobody else can run — they execute back to back.
    # Fix for real blocking code: await asyncio.to_thread(time.sleep, secs).


if __name__ == "__main__":
    asyncio.run(main())
