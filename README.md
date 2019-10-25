# pdevops

Pdevops is a highly available build server that takes it build request, runs it and continue to send status updates via websocket. 
The entire system is implemented in python usingh websockets + celery. 


## Rabbitmq setup

sudo docker run -d --hostname my-rabbit --name some-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3-management


To install 
python -m pip install pika --upgrade

# Setup scripts for testing purposes 
# python BuildConsumer.py 

# command to run
# gunicorn --bind 0.0.0.0:8888 FalconRestService:api

# curl command 
# curl -d '{"id":"123456"}' -H "Content-Type: application/json" -X POST http://localhost:8888/queuebuildrequest


## Setup Mongodb

## Kafka setup 




sudo docker network create -d overlay --attachable kafka-net

sudo docker service create --network kafka-net --name=zookeeper \
          --publish 2181:2181 qnib/plain-zookeeper:2018-04-25

sudo docker service create --network kafka-net --name=zkui \
          --publish 9090:9090 \
          qnib/plain-zkui@sha256:30c4aa1236ee90e4274a9059a5fa87de2ee778d9bfa3cb48c4c9aafe7cfa1a13


 sudo docker service create --network kafka-net --name broker          --hostname="{{.Service.Name}}.{{.Task.Slot}}.{{.Task.ID}}"          -e KAFKA_BROKER_ID={{.Task.Slot}} -e ZK_SERVERS=tasks.zookeeper          qnib/plain-kafka:2019-01-28_2.1.0












