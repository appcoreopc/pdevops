# from messageQueue import *

import messageQueue

from AppConstants import BUILDREQUESTQUEUE, TARGETSERVER, FAN_OUT
from processWorker.runner import ProcessRunner
from model.QueuConfiguration import QueueConfiguration, QueueType
import logging

## This is the command / scripts  builder 
## It takes pipeline id, and runs commands and writes output to the status queue.

class BuildConsumer:
    
    def __init__(self):
        pass

    def start(self):
        print("Starting up build consumer")
        queueTransport =  messageQueue.RabbitMqReader(TARGETSERVER, BUILDREQUESTQUEUE)
        buildProcessRunner = ProcessRunner()
        queueType = QueueConfiguration(FAN_OUT, BUILDREQUESTQUEUE)
        queueManager = messageQueue.QueueManager(queueTransport, buildProcessRunner, queueType)
        queueManager.read()

if __name__ == '__main__':
    logging.info("starting up")
    consumer = BuildConsumer()
    consumer.start()