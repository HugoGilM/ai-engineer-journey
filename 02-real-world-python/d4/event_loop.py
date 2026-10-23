import asyncio


async def job(name: str, secs: int) -> None:
    print(f"start {name}")
    await asyncio.sleep(secs)
    print(f"end {name}")


async def main() -> None:
    await asyncio.gather(job("A", 2), job("B", 1))


asyncio.run(main())
