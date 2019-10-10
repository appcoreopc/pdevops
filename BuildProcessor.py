from messageQueue.RabbitMqComponent import RabbitMqComponent
from messageQueue.QueueManager import QueueManager

# sudo docker run -p 5672:5672 -p 15672:15672 -d --hostname my-rabbit --name some-rabbit rabbitmq:3-management

## Setup 

queueTransport = RabbitMqComponent("localhost", "hello")

queueManager = QueueManager(queueTransport)
queueManager.publish("testing testing")
queueManager.publish("testing testing")
queueManager.publish("testing testing")




queueManager.read()

### 
