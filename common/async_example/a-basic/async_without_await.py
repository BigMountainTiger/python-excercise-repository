import asyncio

async def func_A():
    result = await func_B()    
    print(result)


async def func_B():
    return 'From an async function that does not await anything'

if __name__ == '__main__':
    asyncio.run(func_A())

    print()
    print('1. You can only await an async function() - awaitable object (Coroutines, tasks, futures)')
    print('2. The await keyword is only allowed in an async function')
    print('3. But it is OK that an async funtion does not await anything')