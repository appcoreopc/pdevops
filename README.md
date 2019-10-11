# pdevops

Pdevops is a highly available build server that takes it build request, runs it and continue to send status updates via websocket. 
The entire system is implemented in python usingh websockets + celery. 


## Rabbitmq setup

sudo docker run -d -p 5672:5672 rabbitmq


To install 
python -m pip install pika --upgrade



## Kafka setup 


sudo docker network create -d overlay --attachable kafka-net

sudo docker service create --network kafka-net --name=zookeeper \
          --publish 2181:2181 qnib/plain-zookeeper:2018-04-25

sudo docker service create --network kafka-net --name=zkui \
          --publish 9090:9090 \
          qnib/plain-zkui@sha256:30c4aa1236ee90e4274a9059a5fa87de2ee778d9bfa3cb48c4c9aafe7cfa1a13


 sudo docker service create --network kafka-net --name broker          --hostname="{{.Service.Name}}.{{.Task.Slot}}.{{.Task.ID}}"          -e KAFKA_BROKER_ID={{.Task.Slot}} -e ZK_SERVERS=tasks.zookeeper          qnib/plain-kafka:2019-01-28_2.1.0






