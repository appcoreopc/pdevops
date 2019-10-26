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

import asyncio
from concurrent.futures import ThreadPoolExecutor
_executor = ThreadPoolExecutor(10)

#  agent/status
#  build/status
#  release/status

BUILD_STATUS_PATH = "/BUILD/STATUS"
RELEASE_STATUS_PATH = "/RELEASE/STATUS"

localwebsocket = None
connection = None
channel = None
bodyData = None

async def sendSocketData(msg):
   print('running sendsocketdata')
   global localwebsocket
   await localwebsocket.send(msg)

async def in_thread(func):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(_executor, func)


async def sendMessages(websocket, content):
  print('calling asyn command')
  await websocket.send(content)

def receiveMessageHandler(chann, method, properties, body):    
    global localwebsocket
    global bodyData 
    print("Data %r" % body)
    if localwebsocket == None:
        print("stop sending")
    else:
        bodyData = body
        print("start sending")
        asyncio.run(localwebsocket.send(body))
        #sendSocketData(localwebsocket, body)
        #asyncio.run(sendSocketData)
        #result = asyncio.gather(sendSocketData(body))

def readStatusQueue():  

      print('##thread', threading.get_ident())
      connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
      channel = connection.channel()
      result = channel.queue_declare(queue='', exclusive=True)
      queue_name = result.method.queue
      print("###async qeue - logging basic queue info", STATUSDATAQUEUE, queue_name)

      channel.queue_bind(exchange=STATUSDATAQUEUE, queue=queue_name)
      channel.basic_consume(queue=queue_name, on_message_callback=receiveMessageHandler, auto_ack=True)
      channel.start_consuming()
      
      print("initialization completed!")


async def ServiceHandler(websocket, path):
    
    global localwebsocket 
    localwebsocket = websocket
    print("current path", path, localwebsocket)

    if path.upper() == BUILD_STATUS_PATH:
      
      #readStatusQueue()    
      #results = await asyncio.gather(
      #   in_thread(readStatusQueue) 
      # )

      ## Running in another thread ##
      loop = asyncio.get_event_loop()
      await loop.run_in_executor(_executor, readStatusQueue)


      #print(results)

      while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)
      
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
                         


                         
start_server = websockets.serve(ServiceHandler, "127.0.0.1", 9001)
print("setting websocket server")

instanceLoop = asyncio.get_event_loop()
asyncio.set_event_loop(instanceLoop)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

print("done!")