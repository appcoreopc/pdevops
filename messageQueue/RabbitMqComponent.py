import pika
from messageQueue.QueueComponent import QueueComponent
from ProcessWorker.Runner import ProcessRunner
from model.QueuConfiguration import QueueConfiguration

class RabbitMqComponent(QueueComponent):

    def receiveMessageHandler(self, chann, method, properties, body):
        print("[x] Received %r" % body)
        print(type(self.processRunner))
        self.processRunner.execute(body)
        
       
    def __init__(self, host: str, targetqueue : str):        
        self.queue = targetqueue
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.processRunner = None
        #self._createQueue(targetqueue)
        # self.channel.basic_consume(self.queue, on_message_callback = self.receiveMessageHandler, auto_ack=True)
  
    def publish(self, message : str):
        print("sending to", self.queue)
        self.channel.basic_publish(exchange=self.queueType.targetName, routing_key='', body=message)

    def read(self):
        print('setting readvalue')    
        result = self.channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        self.channel.queue_bind(exchange=self.queueType.targetName, queue=queue_name)
        self.channel.start_consuming()
        
    def _createQueue(self, targetqueue : str):
        self.channel.queue_declare(queue=targetqueue)

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


