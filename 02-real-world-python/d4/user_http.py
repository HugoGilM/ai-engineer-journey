import asyncio

import httpx
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str


async def get_user(client: httpx.AsyncClient, user_id: int) -> User:
    resp = await client.get(f"/users/{user_id}")
    resp.raise_for_status()  # like EnsureSuccessStatusCode()
    return User.model_validate_json(resp.content)


async def main() -> None:
    async with httpx.AsyncClient(
        base_url="https://jsonplaceholder.typicode.com",
        timeout=10.0,
    ) as client:
        user = await get_user(client, 1)
        print(user)


asyncio.run(main())  # entry point: starts the event loop, like async Task Main()
