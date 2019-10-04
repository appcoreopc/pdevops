import asyncio
import datetime
import random
import websockets
import http

 
#  agent/status
#  build/status
#  release/status
#  
BUILD_STATUS_PATH = "BUILD/STATUS"
RELEASE_STATUS_PATH = "RELEASE/STATUS"

async def time(websocket, path):
    print("current path", path)
    if path.upper() == BUILD_STATUS_PATH:
      while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

    elif path.upper() == RELEASE_STATUS_PATH:
      while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "127.0.0.1", 9001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()