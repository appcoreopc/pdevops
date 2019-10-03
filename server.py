import asyncio
import datetime
import random
import websockets
import http

# async def health_check(path, request_headers):
 
#     if path == "/health/":
#         print(type(path))
#         print(type(request_headers))
#         while True:
#             now = datetime.datetime.utcnow().isoformat() + "Z"
#             #await websocket.send(now)
#             await asyncio.sleep(random.random() * 3)


async def time(websocket, path):
    print("currentpath")
    print(path)    
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "127.0.0.1", 9001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()