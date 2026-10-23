import asyncio


async def fetch_data(n: int) -> int:
    await asyncio.sleep(1)  # like await Task.Delay(1000)
    return n * 2


async def main() -> None:
    result = await fetch_data(5)
    print(result)


asyncio.run(main())  # entry point: starts the event loop, like async Task Main()
