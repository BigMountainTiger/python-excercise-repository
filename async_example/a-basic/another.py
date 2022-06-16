import asyncio
from fnmatch import fnmatch

async def func_A():
    print('A')


async def main():

    crt = func_A()
    print('Coroutine is called');
    
    await crt

asyncio.run(main())
