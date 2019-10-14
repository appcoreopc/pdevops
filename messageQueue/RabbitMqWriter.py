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
        print("Sending to", self.queue)
        self.channel.basic_publish(exchange=self.queueType.targetName, routing_key='', body=message)

    # def read(self):
    #     print('setting read queue for fan out, ', self.queueType.targetName)   
    #     result = self.channel.queue_declare(queue='', exclusive=True)
    #     queue_name = result.method.queue
    #     print("randon queue name", queue_name)
    #     self.channel.queue_bind(exchange=self.queueType.targetName, queue=queue_name)
    #     self.channel.basic_consume(queue=queue_name, on_message_callback=self.receiveMessageHandler, auto_ack=True)
    #     self.channel.start_consuming()
    
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


