from messageQueue.QueueComponent import QueueComponent 
from ProcessWorker.Runner import ProcessRunner


class QueueManager():
    def __init__(self, queueComponent : QueueComponent):
        self.queueComponent = queueComponent
     
    def publish(self, message : str):
        self.queueComponent.publish(message)

    def read(self, processRunner : ProcessRunner):
        self.queueComponent.read(processRunner)

    def close(self):
        self.close()
        
