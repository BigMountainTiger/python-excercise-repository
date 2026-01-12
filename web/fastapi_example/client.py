import time
import asyncio
import aiohttp


async def http_get(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()

    return html


async def call():

    tasks = []
    for i in range(0, 10):

        # Both task and coroutine work with gather

        # tasks.append(asyncio.create_task(
        #     http_get(f'http://127.0.0.1:8000/items/{i}?q=abcd')))

        tasks.append(http_get(f'http://127.0.0.1:8000/items/{i}?q=abcd'))

    results = await asyncio.gather(*tasks)
    return results


if __name__ == '__main__':

    start_time = time.time()
    results = asyncio.run(call())

    print(f'All http calls completed in {(time.time() - start_time)} seconds')

    for r in results:
        print(r)
