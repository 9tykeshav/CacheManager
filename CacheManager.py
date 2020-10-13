import time

import asyncio

class CacheManager :

    def __init__(self, loop ) :

        self.ttl = {}

        self.cache = {}

        self.loop = loop

        self.loop.create_task(self.cleanup())

    def set(self , key , value ) :

        self.cache[key] = value

    def get (self , key ) :

        return self.cache.get(key)

    def tset (self , key , value , ttl: int ) :

        self.ttl[key] = time.time() + ttl

        self.cache[key] = value

    async def cleanup(self) :

        while True and not len( self.ttl) == 0  :

          await asyncio.sleep(2)

          for x , y  in self.ttl.copy().items() :

            if y <= time.time() :

                 self.cache.pop(x)

                 self.ttl.pop(x)
