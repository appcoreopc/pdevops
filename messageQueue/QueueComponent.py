from ProcessWorker.Runner import ProcessRunner

class QueueComponent:
    
    def __init__(self):
        pass

    def connect(self, connectionString : str):
        pass
    
    def publish(self, message : str):
        pass

    def read(self):
        pass

    def configureRunner(self, processRunner : ProcessRunner):
        pass