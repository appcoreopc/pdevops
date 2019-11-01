from processWorker.runner import ProcessRunner
from model.QueuConfiguration import QueueConfiguration

class QueueComponent:
    
    def __init__(self):
        pass

    def connect(self, connectionString : str):
        pass
    
    def publish(self, message : str):
        pass

    def read(self):
        pass

    def configureRunner(self, processRunner : ProcessRunner, QueueComponent, queueConfig : QueueConfiguration):
        pass