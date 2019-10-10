
import pika
import messageQueue.QueueComponent

class RabbitMqComponent(QueueCompoent):
    def __init__(self, host: str, targetqueue : str ):
        self.queue = targetqueue
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
    
    def publish(self, message : str):
        self.channel.basic_publish(exchange='', routing_key=self.queue, body=message)

    def read(self):
        self.channel.basic_consume(self.queue, auto_ack=True, on_message_callback=_receiveMessageHandler)
    
    def _receiveMessageHandler(self, ch, method, properties, body):
        print(" [x] Received %r" % body)
    
