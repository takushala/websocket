import asyncio
import websockets
import subprocess

async def response(websocket, path):
    msg = await websocket.recv()
    print(f"We got it: {msg}")
    await websocket.send("lul")
    test(msg)
    if (msg=="stopp"):
        subprocess.call([r'C:\\Users\\takus\\Desktop\\websocket\\kill.bat'], shell=True)
        
def test(str): 
    print(str)

start_server = websockets.serve(response, 'localhost', 1234)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()