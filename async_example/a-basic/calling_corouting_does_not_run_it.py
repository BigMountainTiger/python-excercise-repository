import asyncio


async def func_2():

    print('Entering func_2, starting to await the asyncio.sleep(1)')
    await asyncio.sleep(1)
    print('Completing func_2')


async def func_1():

    a_coroutine = func_2()
    print('Created the coroutine instance, calling the coroutine function does not run it at all')
    print()
    await a_coroutine

    print('Completed the await')


def run():
    asyncio.run(func_1())


if __name__ == '__main__':

    run()
