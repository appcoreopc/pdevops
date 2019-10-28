import asyncio
import websockets
import datetime


async def hello(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(1) 
  

start_server = websockets.serve(hello, "localhost", 9002)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()