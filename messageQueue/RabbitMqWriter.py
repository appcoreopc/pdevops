import pika
from messageQueue.QueueComponent import QueueComponent
from ProcessWorker.Runner import ProcessRunner
from model.QueuConfiguration import QueueConfiguration

class RabbitMqWriter(QueueComponent):
       
    def __init__(self, host: str, targetqueue : str):        
        self.queue = targetqueue
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.processRunner = None
     
    def publish(self, message : str):
        print("Sending to exchange", self.queueType.targetName)
        self.channel.basic_publish(exchange=self.queueType.targetName, routing_key='', body=message)

    def configure(self, processRunner, queueType):
        self.processRunner = processRunner
        self.configureQueueType(queueType)
    
    def configureQueueType(self, queueType: QueueConfiguration):
        self.queueType = queueType
        print("info setup")
        print(queueType.targetName, queueType.queueType)
        if queueType.targetName:        
         print("setting up exchange", queueType.targetName, queueType.queueType)
         self.channel.exchange_declare(exchange=queueType.targetName, exchange_type=queueType.queueType)

    def close(self):
        self.channel.close()

    def __exit__(self):
        self.channel.close()


