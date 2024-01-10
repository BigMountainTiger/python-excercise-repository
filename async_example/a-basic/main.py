import asyncio

async def func_1():
    # A call to a coroutine returns a coroutine object
    f = func_2()
    print('After creation of the coroutine object')
    await f

    task = asyncio.create_task(func_2())
    value = await task
    print(value)

    task = asyncio.create_task(func_3('In task', 1))
    # await task
    await func_3('By await', 1)

    print('What is this')

    return 'This is the return value'


async def func_2():
    print('Starting func_2')
    await asyncio.sleep(1)
    print('In func_2')

    return 'Return value from func_2'

async def func_3(text, t):
    print(f'Entering func_3 - {text}')
    await asyncio.sleep(t)
    print(f'In func_3 - {text}')

if __name__ == '__main__':
    
    result = asyncio.run(func_1())
    print(result)
    print(f'Here - {result}')