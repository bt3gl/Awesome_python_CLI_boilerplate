#!/usr/bin/env python3

import asyncio

async def delayed_hello():
    print("Hello ")
    await asyncio.sleep(1)
    print("World!")


if __name__ == "__main__":
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(delayed_hello())
    loop.close()