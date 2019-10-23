import asyncio
import datetime
import random
import websockets
import http
 
from messageQueue.RabbitMqReaderAsync import RabbitMqReaderAsync
from messageQueue.QueueManagerAsync import QueueManagerAsync
from AppConstants import TARGETSERVER, STATUSDATAQUEUE, FAN_OUT
from ProcessWorker.StatusServer import StatusServer
from model.QueuConfiguration import QueueConfiguration, QueueType

#  agent/status
#  build/status
#  release/status
#  
BUILD_STATUS_PATH = "/BUILD/STATUS"
RELEASE_STATUS_PATH = "/RELEASE/STATUS"

localwebsocket = None


def ServiceHandler(websocket, path):

    localwebsocket = websocket

    print("current path", path)

    if path.upper() == BUILD_STATUS_PATH:
      queueTransport = RabbitMqReaderAsync(TARGETSERVER, STATUSDATAQUEUE)
      buildProcessRunner = StatusServer(websocket)
      queueType = QueueConfiguration(FAN_OUT, STATUSDATAQUEUE)
      queueManager = QueueManagerAsync(queueTransport, buildProcessRunner, queueType)
      queueManager.read()

      now = datetime.datetime.utcnow().isoformat() + "Z"
      websocket.send(now)
      asyncio.sleep(random.random() * 3)
   
    elif path.upper() == RELEASE_STATUS_PATH:
      while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        websocket.send(now)
        asyncio.sleep(random.random() * 3)

               

start_server = websockets.serve(ServiceHandler, "127.0.0.1", 9001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()