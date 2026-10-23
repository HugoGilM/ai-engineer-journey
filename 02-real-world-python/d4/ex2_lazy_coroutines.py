"""Exercise 2: lazy coroutines vs hot tasks.

Coroutine vs task in one sentence: a coroutine is a paused recipe that does nothing
until awaited, while a task is that coroutine already scheduled on the event loop
and running on its own (like a hot C# Task).
"""

import asyncio


async def work(name: str, secs: float) -> str:
    """Sleep without blocking the loop, print, then return the name."""
    print(f"  {name}: started")
    await asyncio.sleep(secs)
    print(f"  {name}: finished")
    return name


async def part_a() -> None:
    """Call without await: only a coroutine object is created, nothing runs."""
    coro = work("x", 1)
    print(f"  got {coro!r}, but 'x: started' never printed")
    coro.close()  # without this: RuntimeWarning: coroutine 'work' was never awaited
    # Writing just `work("x", 1)` as a bare statement, mypy --strict reports:
    #   error: Value of type "Coroutine[Any, Any, str]" must be used  [unused-coroutine]
    #   note: Are you missing an await?


async def part_b() -> None:
    """create_task schedules it; sleeping yields to the loop, so it runs."""
    t = asyncio.create_task(work("y", 1))
    await asyncio.sleep(2)
    print(f"  task done? {t.done()} -> result {t.result()!r}")


async def part_c() -> asyncio.Task[str]:
    """create_task, then return immediately: the task never gets a turn."""
    t = asyncio.create_task(work("z", 1))
    return t


async def main() -> None:
    """Run the three parts."""
    print("(a) call without await")
    await part_a()

    print("(b) create_task + sleep(2)")
    await part_b()


def run_part_c() -> None:
    """Run part c as its own asyncio.run so the shutdown behaviour is visible."""
    print("(c) create_task + return immediately")
    t = asyncio.run(part_c())
    # asyncio.run cancels every pending task before closing the loop. "z: started"
    # still prints because the cancelled task gets one final step, but the
    # CancelledError hits its first await, so "z: finished" never appears.
    print(f"  cancelled? {t.cancelled()}")


if __name__ == "__main__":
    asyncio.run(main())
    run_part_c()
