from messageQueue.RabbitMqReader import RabbitMqReader
from messageQueue.QueueManager import QueueManager
from AppConstants import BUILDREQUESTQUEUE, TARGETSERVER, FAN_OUT, BUILD_REQUEST_QUEUE
from ProcessWorker.Runner import ProcessRunner
from model.QueuConfiguration import QueueConfiguration, QueueType

## Setup 

class BuildConsumer:
    
    def __init__(self):
        pass

    def start(self):
        print("Starting up build consumer")
        queueTransport = RabbitMqReader(TARGETSERVER, BUILDREQUESTQUEUE)
        buildProcessRunner = ProcessRunner()
        queueType = QueueConfiguration('fanout', "buildrequest_in")
        queueManager = QueueManager(queueTransport, buildProcessRunner, queueType)
        queueManager.read()




#queueManager.publish("testing testing")
#queueManager.publish("testing testing")
#queueManager.publish("testing testing")
#queueManager.read()

### 
if __name__ == '__main__':
    print("starting up")
    consumer = BuildConsumer()
    consumer.start()