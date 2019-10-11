from messageQueue.RabbitMqComponent import RabbitMqComponent
from messageQueue.QueueManager import QueueManager
from AppConstants import STATUSDATAQUEUE

## Setup 

queueTransport = RabbitMqComponent("localhost", STATUSDATAQUEUE)
queueManager = QueueManager(queueTransport)
queueManager.read()

### 
