from CacheManager import CacheManager

import time

import asyncio

async def main () :

    loop = asyncio.get_event_loop()

    a = CacheManager(loop)

    a.tset("b" , 5, 6 )

    await  asyncio.sleep(3)

    print(a.get("b"))

asyncio.run(main())
