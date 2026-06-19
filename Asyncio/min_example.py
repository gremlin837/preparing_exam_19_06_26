import asyncio
async def print1():
    print(1)
async def print2():
    await asyncio.sleep(10)
    print(2)
async def print3():
    print(3)
async def main():
    t1 = asyncio.create_task(print1())
    t2 = asyncio.create_task(print2())
    t3 = asyncio.create_task(print3())
    # await t1
    # await t2
    # await t3
    await asyncio.gather(t1,t2,t3)
asyncio.run(main())




