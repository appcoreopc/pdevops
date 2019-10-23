from messageQueue.RabbitMqWriter import RabbitMqWriter
from messageQueue.QueueManager import QueueManager
from AppConstants import BUILDREQUESTQUEUE, TARGETSERVER, FAN_OUT
from ProcessWorker.Runner import ProcessRunner
from model.QueuConfiguration import QueueConfiguration, QueueType
import logging


## Setup 

class BuildProcessor:

    def __init__(self):
        pass

    def queueBuild(self, id : str):
        logging.info("queuing request id ", id)
        queueTransport = RabbitMqWriter(TARGETSERVER, BUILDREQUESTQUEUE)
        buildProcessRunner = ProcessRunner()
        queueType = QueueConfiguration(FAN_OUT, BUILDREQUESTQUEUE)
        queueManager = QueueManager(queueTransport, buildProcessRunner, queueType)
        queueManager.publish(id)

