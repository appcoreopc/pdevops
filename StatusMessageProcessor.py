from messageQueue.RabbitMqComponent import RabbitMqComponent
from messageQueue.QueueManager import QueueManager

## Setup 

queueTransport = RabbitMqComponent("localhost", "hello")

queueManager = QueueManager(queueTransport)
queueManager.publish("testing testing")
queueManager.publish("testing testing")
queueManager.publish("testing testing")

queueManager.read()

### 
