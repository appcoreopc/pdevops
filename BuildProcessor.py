from messageQueue.RabbitMqComponent import RabbitMqComponent
from messageQueue.QueueManager import QueueManager


a = RabbitMqComponent("localhost", "hello")
mgr = QueueManager(a)
mgr.publish("testing testing")