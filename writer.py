from messageQueue.RabbitMqWriter import RabbitMqWriter
from messageQueue.QueueManager import QueueManager
from AppConstants import BUILDREQUESTQUEUE, TARGETSERVER
from ProcessWorker.Runner import ProcessRunner
from model.QueuConfiguration import QueueConfiguration, QueueType


# sudo docker run -p 5672:5672 -p 15672:15672 -d --hostname my-rabbit --name some-rabbit rabbitmq:3-management

## Setup 

queueTransport = RabbitMqWriter(TARGETSERVER, BUILDREQUESTQUEUE)
buildProcessRunner = ProcessRunner()
queueType = QueueConfiguration('fanout', "buildrequest_in")

queueManager = QueueManager(queueTransport, buildProcessRunner, queueType)

queueManager.publish("testing testing")
queueManager.publish("testing testing")
queueManager.publish("testing testing")

## queueManager.read()

### 
