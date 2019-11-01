from messageQueue.RabbitMqWriter import RabbitMqWriter
from messageQueue.RabbitMqReader import RabbitMqReader
from messageQueue.QueueManager import QueueManager
from AppConstants import BUILDREQUESTQUEUE, TARGETSERVER, STATUSDATAQUEUE
from processWorker.runner import ProcessRunner
from model.QueuConfiguration import QueueConfiguration, QueueType


# sudo docker run -p 5672:5672 -p 15672:15672 -d --hostname my-rabbit --name some-rabbit rabbitmq:3-management

## Setup 

queueTransport = RabbitMqReader(TARGETSERVER, STATUSDATAQUEUE)
buildProcessRunner = ProcessRunner()
queueType = QueueConfiguration('fanout', STATUSDATAQUEUE)

queueManager = QueueManager(queueTransport, buildProcessRunner, queueType)

# queueManager.publish("testing testing")
# queueManager.publish("testing testing")
# queueManager.publish("testing testing")

queueManager.read()

### 
