import asyncio
import datetime
import random
import websockets
import http
import pika

from messageQueue.RabbitMqReaderAsync import RabbitMqReaderAsync
from messageQueue.QueueManagerAsync import QueueManagerAsync
from appConstants import TARGETSERVER, STATUSDATAQUEUE, FAN_OUT
from processWorker.statusServer import StatusServer
from model.QueuConfiguration import QueueConfiguration, QueueType
import threading

import queue
import logging 

import asyncio

from concurrent.futures import ThreadPoolExecutor
_executor = ThreadPoolExecutor(10)

BUILD_STATUS_PATH = "/BUILD/STATUS"
RELEASE_STATUS_PATH = "/RELEASE/STATUS"

connection = None
channel = None
bodyData = None

processQueue = queue.Queue()

logging.basicConfig(level='INFO')

CLIENTS = set()

async def register(websocket):
    CLIENTS.add(websocket)
    print("registering new client")
    await notify_users()

async def unregister(websocket):
    CLIENTS.remove(websocket)
    print("unregistering client")
    await notify_users()

async def notify_users():
    if CLIENTS:
      while True:
        if not processQueue.empty():  
         message = processQueue.get()
         if message:
           await asyncio.wait([user.send(message) for user in CLIENTS])
        else:
          await asyncio.sleep(2)  

def receiveMessageHandler(chann, method, properties, body):        
    print("QUEUE : Data %r" % body)
    processQueue.put(body.decode("utf-8"))   
   
def readStatusQueue():     
        print('*****Listening to status queue******')
        connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        channel = connection.channel()
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        print("###async queue####", STATUSDATAQUEUE, queue_name)

        channel.queue_bind(exchange=STATUSDATAQUEUE, queue=queue_name)
        channel.basic_consume(queue=queue_name, on_message_callback=receiveMessageHandler, auto_ack=True)
        channel.start_consuming()  

async def ServiceHandler(websocket, path):  
    if path.upper() == BUILD_STATUS_PATH:  
      try:
        await register(websocket)
      finally:
        await unregister(websocket)
           
    elif path.upper() == RELEASE_STATUS_PATH:
      while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        websocket.send(now)
        asyncio.sleep(random.random() * 3)

## read message queue and populate queue
# queueReadingThread = threading.Thread(target=readStatusQueue)
# queueReadingThread.start()

start_server = websockets.serve(ServiceHandler, "127.0.0.1", 9001)

instanceLoop = asyncio.get_event_loop()
asyncio.set_event_loop(instanceLoop)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
