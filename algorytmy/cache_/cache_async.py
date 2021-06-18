import asyncio
from random import randint

# from cachetools import cached

##
from asyncache import cached    # wersja async


from cachetools import TTLCache, LRUCache


@cached(TTLCache(200, 60))  # 1 minute TTL, 200 users
async def foo(x) -> int:
    print('uruchamiam foo')
    return x * x


@cached(cache=LRUCache(maxsize=10))
async def goo(a, b, c) -> int:
    return a + b + c




async def task():
    for i in range(300):
        print(await foo(randint(0, 10)))
        print(await goo(*[1, 1, 8]))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task())