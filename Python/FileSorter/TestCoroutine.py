import os
import sys
import time
import asyncio
import random
from tqdm import tqdm


class job:
    def __init__(self, value):
        self.value = value

    async def work(self):
        print("start : %d" % self.value)
        await asyncio.sleep(self.value)
        # print("end : %d" % self.value)
        return self.value

async def jobLoop(works):
    for w in asyncio.as_completed(works):
        c = await w

async def progressBar(works):
    for w in tqdm( asyncio.as_completed(works), total=len(works) ):
    # for w in tqdm( works, total=len(works) ):
        await w

    # progressBar = tqdm( asyncio.as_completed(works), total=len(works) )
    
    # while not asyncio.as_completed( progressBar ):
    #     await progressBar

works = list()
for i in range( 1, 6 ):
    j = job( random.randint(i, 6) )
    works.append( asyncio.ensure_future(j.work()) )

loop = asyncio.get_event_loop()
loop.run_until_complete( asyncio.gather( jobLoop(works), progressBar(works) ) )
loop.close()


