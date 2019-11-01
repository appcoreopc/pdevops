import pika
from messageQueue.QueueComponent import QueueComponent
from processWorker.runner import ProcessRunner
from model.QueuConfiguration import QueueConfiguration
import logging

class RabbitMqReader(QueueComponent):

    def receiveMessageHandler(self, chann, method, properties, body):
        logging.info("[x] Received %r" % body)
        self.processRunner.execute(body)        
       
    def __init__(self, host: str, targetqueue : str):        
        self.queue = targetqueue
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.processRunner = None
      
    def read(self):
        #try:
            result = self.channel.queue_declare(queue='', exclusive=True)
            queue_name = result.method.queue
            print("logging basic queue info", self.queueType.targetName, queue_name)
            self.channel.queue_bind(exchange=self.queueType.targetName, queue=queue_name)
            self.channel.basic_consume(queue=queue_name, on_message_callback=self.receiveMessageHandler, auto_ack=True)
            self.channel.start_consuming()
        #except:
        #    logging.warning("The underlying queue connection could be closed.")
                   
        
    def configure(self, processRunner, queueType):
        self.processRunner = processRunner
        self.configureQueueType(queueType)
       
    def configureQueueType(self, queueType: QueueConfiguration):
        self.queueType = queueType
        print("basic confguration:", self.queueType.targetName, self.queueType.queueType)
        if queueType.targetName:        
         print("reading data from this exchange", queueType.targetName, queueType.queueType)
         self.channel.exchange_declare(exchange=self.queueType.targetName, exchange_type=self.queueType.queueType)

    def close(self):
        self.channel.close()

    def __exit__(self):
        self.channel.close()


