from messageQueue import *
# from messageQueue.QueueManager import QueueManager

from messageQueue import * 

from AppConstants import BUILDREQUESTQUEUE, TARGETSERVER, FAN_OUT, BUILD_REQUEST_QUEUE
from ProcessWorker.Runner import ProcessRunner
from model.QueuConfiguration import QueueConfiguration, QueueType
import logging

## Setup 

class BuildConsumer:
    
    def __init__(self):
        pass

    def start(self):
        logging.info("Starting up build consumer")
        queueTransport = RabbitMqReader.RabbitMqReader(TARGETSERVER, BUILDREQUESTQUEUE)
        buildProcessRunner = ProcessRunner()
        queueType = QueueConfiguration(FAN_OUT, BUILD_REQUEST_QUEUE)
        queueManager = QueueManager.QueueManager(queueTransport, buildProcessRunner, queueType)
        queueManager.read()

if __name__ == '__main__':
    logging.info("starting up")
    consumer = BuildConsumer()
    consumer.start()