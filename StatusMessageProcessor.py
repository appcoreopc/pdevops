from messageQueue.RabbitMqReader import RabbitMqReader
from messageQueue.QueueManager import QueueManager
from AppConstants import STATUSDATAQUEUE

## Setup 

queueTransport = RabbitMqReader("localhost", STATUSDATAQUEUE)
queueManager = QueueManager(queueTransport)
queueManager.read()

### 
