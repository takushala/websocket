import asyncio
import websockets

async def request():
    msg = input('Your msg here: ')
    while (msg!='stop'):
        async with websockets.connect("ws://localhost:1234") as ws:
            await ws.send(msg)
            print(await ws.recv())
            msg = input('Another one: ')
            await ws.send(msg)
            if (msg=="stop"):
                await ws.close()

asyncio.get_event_loop().run_until_complete(request())