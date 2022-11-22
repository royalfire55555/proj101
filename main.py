import random
import asyncio

vals = []


async def updateVal():
    while len(vals) < 5:
        vals.append(random.randint(1, 6))

while True:
    if len(vals) < 5:
        asyncio.run(updateVal())

    input("Press ctrl+c to exit, and enter to roll a die")
    print(vals[0])
    vals.remove(vals[0])
