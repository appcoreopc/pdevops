import pika
from messageQueue.QueueComponent import QueueComponent
from ProcessWorker.Runner import ProcessRunner
from model.QueuConfiguration import QueueConfiguration

class RabbitMqReader(QueueComponent):

    def receiveMessageHandler(self, chann, method, properties, body):
        print("[x] Received %r" % body)
        print(type(self.processRunner))
        self.processRunner.execute(body)        
       
    def __init__(self, host: str, targetqueue : str):        
        self.queue = targetqueue
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.processRunner = None
      
    def read(self):
        result = self.channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        self.channel.queue_bind(exchange=self.queueType.targetName, queue=queue_name)
        self.channel.basic_consume(queue=queue_name, on_message_callback=self.receiveMessageHandler, auto_ack=True)
        self.channel.start_consuming()
        
    def configure(self, processRunner, queueType):
        self.processRunner = processRunner
        self.configureQueueType(queueType)
       
    def configureQueueType(self, queueType: QueueConfiguration):
        self.queueType = queueType
        print("info setup")
        print(queueType.targetName, queueType.queueType)
        if queueType.targetName:        
         print("setting up exchange", queueType.targetName, queueType.queueType)
         self.channel.exchange_declare(exchange=queueType.targetName, exchange_type='fanout')

    def close(self):
        self.channel.close()

    def __exit__(self):
        self.channel.close()


