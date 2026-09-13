import asyncio
from typing import Awaitable

import aiohttp


async def semaphore_wrapper(coroutine: Awaitable, sem: asyncio.Semaphore):
    print("Запускаем корутину")
    async with sem:
        print("Забираем 1 семафор")
        return await coroutine


async def fetch_one(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as response:
        return await response.json()


async def fetch_all(urls: list[str], limit: int) -> list[str | None]:
    sem = asyncio.Semaphore(limit)
    async with aiohttp.ClientSession(raise_for_status=True) as session:
        results = await asyncio.gather(
            *[semaphore_wrapper(fetch_one(session, url), sem) for url in urls]
        )
        return results


async def main() -> None:
    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
        "https://jsonplaceholder.typicode.com/todos/4",
        "https://jsonplaceholder.typicode.com/todos/5",
        "https://jsonplaceholder.typicode.com/todos/6",
        "https://jsonplaceholder.typicode.com/todos/7",
        "https://jsonplaceholder.typicode.com/todos/8",
        "https://jsonplaceholder.typicode.com/todos/9",
        "https://jsonplaceholder.typicode.com/todos/10"
    ]

    limit = 2

    results = await fetch_all(urls, limit)
    print(results)


if __name__ == '__main__':
    asyncio.run(main())
