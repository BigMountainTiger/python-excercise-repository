import asyncio

async def exception_func():
    raise Exception('An exception thrown')

async def run():
    
    try:
        await exception_func()
    except Exception as e:
        print(e)

    try:
        await exception_func()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    
    asyncio.run(run())
    print('Done event loop')