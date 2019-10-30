# pdevops

Pdevops is a highly available build server that runs builds, It sends output from console and stream it into a queue, line by line and provides websocket based updated to client connected to it.

The entire system is implemented in python usingh websockets + rabbitmq + asyncio + threading.

## Rabbitmq setup

sudo docker run -d --hostname my-rabbit --name some-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3-management


To install 
python -m pip install pika --upgrade

### Setup scripts for testing purposes 

Create a terminal and then run tghe following command :- 


1.python BuildConsumer.py 

2.gunicorn --bind 0.0.0.0:8888 FalconRestService:api

3. curl -d '{"id":"123456"}' -H "Content-Type: application/json" -X POST http://localhost:8888/queuebuildrequest

4. python ws_server.py 

5. run index.html 








