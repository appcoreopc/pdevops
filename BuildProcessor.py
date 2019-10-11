from messageQueue.RabbitMqComponent import RabbitMqComponent
from messageQueue.QueueManager import QueueManager
from AppConstants import BUILDREQUESTQUEUE

# sudo docker run -p 5672:5672 -p 15672:15672 -d --hostname my-rabbit --name some-rabbit rabbitmq:3-management

## Setup 

class Test:
    def __init__(self):
        print("init")

queueTransport = RabbitMqComponent("localhost", BUILDREQUESTQUEUE)

queueManager = QueueManager(queueTransport)
queueManager.publish("testing testing")
queueManager.publish("testing testing")
queueManager.publish("testing testing")

queueManager.read()

### 
