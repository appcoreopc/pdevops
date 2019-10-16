from messageQueue.RabbitMqWriter import RabbitMqWriter
from messageQueue.QueueManager import QueueManager
from AppConstants import BUILDREQUESTQUEUE, TARGETSERVER, FAN_OUT, BUILD_REQUEST_QUEUE
from ProcessWorker.Runner import ProcessRunner
from model.QueuConfiguration import QueueConfiguration, QueueType

## Setup 

class BuildProcessor:

    def __init__(self):
        pass

    def queueBuild(self, id : str):
        print("queuing request id ", id)
        queueTransport = RabbitMqWriter(TARGETSERVER, BUILDREQUESTQUEUE)
        buildProcessRunner = ProcessRunner()
        queueType = QueueConfiguration('fanout', "buildrequest_in")
        queueManager = QueueManager(queueTransport, buildProcessRunner, queueType)
        queueManager.publish(id)

#queueManager.publish("testing testing")
#queueManager.publish("testing testing")
#queueManager.publish("testing testing")
#queueManager.read()

### 
