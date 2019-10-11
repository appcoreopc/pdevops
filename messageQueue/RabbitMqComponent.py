
import pika
from messageQueue.QueueComponent import QueueComponent
from ProcessWorker.Runner import ProcessRunner

class RabbitMqComponent(QueueComponent):

    def receiveMessageHandler(self, chann, method, properties, body):
        print(" [x] Received %r" % body)
        print(type(self.processRunner))
        self.processRunner.execute(body)
        
       
    def __init__(self, host: str, targetqueue : str):
        
        self.queue = targetqueue
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))

        self.channel = self.connection.channel()
        self.processRunner = None
        self._createQueue(targetqueue)

        self.channel.basic_consume(self.queue, on_message_callback = self.receiveMessageHandler, auto_ack=True)
           
    def publish(self, message : str):
        print("sending to", self.queue)
        self.channel.basic_publish(exchange='', routing_key=self.queue, body=message)

    def read(self, runner :  ProcessRunner):
        print('setting readvalue')
        self.processRunner = runner 
        self.channel.start_consuming()
        
    def _createQueue(self, targetqueue : str):
        self.channel.queue_declare(queue=targetqueue)

    def close(self):
        self.channel.close()

    def __exit__(self):
        self.channel.close()


