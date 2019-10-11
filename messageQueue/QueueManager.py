from messageQueue.QueueComponent import QueueComponent 
from ProcessWorker.Runner import ProcessRunner

class QueueManager():
    def __init__(self, queueComponent : QueueComponent, processRuner : ProcessRunner):
        self.queueComponent = queueComponent
        self.processRunner = processRuner
        self.queueComponent.configureRunner(processRuner)
     
    def publish(self, message : str):
        self.queueComponent.publish(message)

    def read(self):
        self.queueComponent.read()

    def close(self):
        self.close()
        
