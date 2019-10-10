
import pika
from messageQueue.QueueComponent import QueueComponent

class RabbitMqComponent(QueueComponent):

    def __receiveMessageHandler(self, chann, method, properties, body):
        print(" [x] Received %r" % body)
       
    def __init__(self, host: str, targetqueue : str):
        
        self.queue = targetqueue
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))

        self.channel = self.connection.channel()

        self._createQueue(targetqueue)

        self.channel.basic_consume(self.queue, on_message_callback = self.__receiveMessageHandler, auto_ack=True)
           
    def publish(self, message : str):
        self.channel.basic_publish(exchange='', routing_key=self.queue, body=message)

    def read(self):
        self.channel.start_consuming()
    
    def _createQueue(self, targetqueue : str):
        self.channel.queue_declare(queue=targetqueue)

    def close(self):
        self.channel.close()

    def __exit__(self):
        self.channel.close()


