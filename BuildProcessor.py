from messageQueue.RabbitMqReader import RabbitMqReader
from messageQueue.QueueManager import QueueManager
from AppConstants import BUILDREQUESTQUEUE, TARGETSERVER
from ProcessWorker.Runner import ProcessRunner
from model.QueuConfiguration import QueueConfiguration, QueueType

## Setup 

queueTransport = RabbitMqReader(TARGETSERVER, BUILDREQUESTQUEUE)
buildProcessRunner = ProcessRunner()
queueType = QueueConfiguration('fanout', "buildrequest_in")
queueManager = QueueManager(queueTransport, buildProcessRunner, queueType)

#queueManager.publish("testing testing")
#queueManager.publish("testing testing")
#queueManager.publish("testing testing")
#queueManager.read()

### 
