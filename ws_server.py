import asyncio
import datetime
import random
import websockets
import http
import pika

from messageQueue.RabbitMqReaderAsync import RabbitMqReaderAsync
from messageQueue.QueueManagerAsync import QueueManagerAsync
from AppConstants import TARGETSERVER, STATUSDATAQUEUE, FAN_OUT
from ProcessWorker.StatusServer import StatusServer
from model.QueuConfiguration import QueueConfiguration, QueueType

import asyncio
from concurrent.futures import ThreadPoolExecutor
_executor = ThreadPoolExecutor(10)

#  agent/status
#  build/status
#  release/status
#  
BUILD_STATUS_PATH = "/BUILD/STATUS"
RELEASE_STATUS_PATH = "/RELEASE/STATUS"

localwebsocket = None
connection = None
channel = None
bodyData = None


async def sendSocketData(msg):
   print(msg)
   global localwebsocket
   await localwebsocket.send(msg)

async def in_thread(func):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(_executor, func)

def receiveMessageHandler(chann, method, properties, body):
    
    global localwebsocket
    global bodyData 
    print("Data %r" % body)
    print(type(localwebsocket))
    if localwebsocket == None:
        print("stop sending")
    else:
        bodyData = body
        print("start sending")
        #sendSocketData(localwebsocket, body)
        asyncio.run(sendSocketData(body))

def readStatusQueue():

      connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
      channel = connection.channel()
      result = channel.queue_declare(queue='', exclusive=True)
      queue_name = result.method.queue
      print("async qeue - logging basic queue info", STATUSDATAQUEUE, queue_name)

      channel.queue_bind(exchange=STATUSDATAQUEUE, queue=queue_name)
      channel.basic_consume(queue=queue_name, on_message_callback=receiveMessageHandler, auto_ack=True)
      channel.start_consuming()
      
      print("initialization completed!")


async def ServiceHandler(websocket, path):

    global localwebsocket 
    localwebsocket = websocket
    print("current path", path, localwebsocket)

    if path.upper() == BUILD_STATUS_PATH:
      readStatusQueue()
     
      # results = await asyncio.gather(
      #   in_thread(readStatusQueue()), 
      # )
      #print(results)
      
    #   now = datetime.datetime.utcnow().isoformat() + "Z"
    #   websocket.send(now)
    #   asyncio.sleep(random.random() * 3)
   
    elif path.upper() == RELEASE_STATUS_PATH:
      while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        websocket.send(now)
        asyncio.sleep(random.random() * 3)

               
start_server = websockets.serve(ServiceHandler, "127.0.0.1", 9001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()