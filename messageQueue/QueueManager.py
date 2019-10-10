from messageQueue.QueueComponent import QueueComponent 

#
# 
#

class QueueManager():
    def __init__(self, queueComponent : QueueComponent):
        self.queueComponent = queueComponent
     
    def publish(self, message : str):
        self.queueComponent.publish(message)

    def read(self):
        self.queueComponent.read()
        
