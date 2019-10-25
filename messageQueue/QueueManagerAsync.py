from messageQueue.QueueComponent import QueueComponent 
from ProcessWorker.Runner import ProcessRunner
from model.QueuConfiguration import QueueConfiguration

class QueueManagerAsync():
    def __init__(self, queueComponent : QueueComponent, processRuner : ProcessRunner, queueconfig : QueueConfiguration):
        self.queueComponent = queueComponent
        self.processRunner = processRuner
        self.queueComponent.configure(processRuner, queueconfig)
     
    def publish(self, message : str):
        self.queueComponent.publish(message)

    def read(self):
        self.queueComponent.read()

    def close(self):
        self.close()
        
