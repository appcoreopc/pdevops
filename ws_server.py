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
import threading

import queue
import logging 

import asyncio

from concurrent.futures import ThreadPoolExecutor
_executor = ThreadPoolExecutor(10)

#  agent/status
#  build/status
#  release/status

#  seems like we have a concurrency issues.

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
    await notify_users()

async def unregister(websocket):
    CLIENTS.remove(websocket)
    await notify_users()

async def notify_users():
    if CLIENTS:
      while True:
        if not processQueue.empty():  
         message = processQueue.get()
         if message:
           await asyncio.wait([user.send(message) for user in CLIENTS])
        else:
          asyncio.sleep(2)  

async def sendSocketData(websocket):

   global processQueue 
   ## while not empty 
   #while not processQueue.empty():
   while True:
     queuedata = processQueue.get()
     print("SOCKET", queuedata)
     await websocket.send(queuedata)
     await asyncio.sleep(1)
     print("SOCKET", processQueue.qsize())

async def in_thread(func):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(_executor, func)

async def sendMessages(websocket, content):
  print('calling asyn command')
  await websocket.send(content)

def receiveMessageHandler(chann, method, properties, body):        
    print("QUEUE : Data %r" % body)
    processQueue.put(body.decode("utf-8"))
    #print("queue size : ", processQueue.qsize())

    #####################################
    # print("Data %r" % body)
    # if localwebsocket == None:
    #     print("stop sending")
    # else:
    #     bodyData = body
    #     print("start sending", type(body))
    #     asyncio.run(localwebsocket.send(body.decode("utf-8")))
    #####################################

def readStatusQueue():  
     
      #global channel
      #if channel == None:
        print('*****Listening to status queue')
        connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        channel = connection.channel()
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        print("###async qeue", STATUSDATAQUEUE, queue_name)

        channel.queue_bind(exchange=STATUSDATAQUEUE, queue=queue_name)
        channel.basic_consume(queue=queue_name, on_message_callback=receiveMessageHandler, auto_ack=True)
        channel.start_consuming()
  

async def ServiceHandler(websocket, path):    
  
    if path.upper() == BUILD_STATUS_PATH:
      
      #readStatusQueue()    
      #results = await asyncio.gather(
      #   in_thread(readStatusQueue) 
      # )

      ## Running in another thread ##

      #if processQueue.empty():
        #print("Binds to queue service")
        #loop = asyncio.get_event_loop()
        #await loop.run_in_executor(_executor, readStatusQueue)

      # print("sleeping state")
      # await asyncio.sleep(2)
      # logging.info("MESSAGE TO CLIENT")
      # await sendSocketData(websocket)

      try:
        await register(websocket)

      finally:
        await unregister(websocket)
        

      # else:
      #   print("sending messages directly to clients")
      #   await websocket.send(processQueue.get())

      #print(results)

      # while True:
      #   now = datetime.datetime.utcnow().isoformat() + "Z"
      #   await websocket.send(now)
      #   await asyncio.sleep(random.random() * 3)
      
    #   now = datetime.datetime.utcnow().isoformat() + "Z"
    #   websocket.send(now)
    #   asyncio.sleep(random.random() * 3)
   
    elif path.upper() == RELEASE_STATUS_PATH:
      while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        websocket.send(now)
        asyncio.sleep(random.random() * 3)

## this is where you already called get_event_loop() 
#loop = asyncio.new_event_loop()
#loop.call_later(5, readStatusQueue, loop)
#asyncio.set_event_loop(loop) # <----
#asyncio.ensure_future(readStatusQueue(loop))
#loop.run_until_complete(readStatusQueue(loop))
#loop.run_until_complete()

## read message queue and populate queue
queueReadingThread = threading.Thread(target=readStatusQueue)
queueReadingThread.start()

start_server = websockets.serve(ServiceHandler, "127.0.0.1", 9001)
print("starting websocket server")

instanceLoop = asyncio.get_event_loop()
asyncio.set_event_loop(instanceLoop)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
