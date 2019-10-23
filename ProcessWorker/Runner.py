#
#
# Runs a process 
#
# python ways of reliable executing cli / command 
# stream output to queue 
# 
# Streaming 
# io.BytesIO or io.BufferedReader

import subprocess 
import time
import logging
import sys

modulename = 'messageQueue'

if modulename not in sys.modules:
    #from messageQueue import *       
    print('You have not imported the {} module'.format(modulename))

#import messageQueue 
import messageQueue 
from AppConstants import BUILDREQUESTQUEUE, TARGETSERVER, FAN_OUT, STATUSDATAQUEUE
from model.QueuConfiguration import QueueConfiguration, QueueType

class ProcessRunner:

    def execute(self, command: str) -> bool:

        queueTransport = messageQueue.RabbitMqWriter(TARGETSERVER, STATUSDATAQUEUE)
        buildProcessRunner = ProcessRunner()
        queueType =  QueueConfiguration(FAN_OUT, STATUSDATAQUEUE)
        self.queueManager = messageQueue.QueueManager(queueTransport, buildProcessRunner, queueType)

        logging.info("executing", command)
        self.streamedOutput = subprocess.Popen(['cat', 'r.csv'], stdout = subprocess.PIPE)
        self.sendOutput(self.streamedOutput) 

    def confgureTargetOut(self):
        pass

    ## Stream output from the command line 
    ## for optimization purposes
    def sendOutput(self, streamedOutput):
        
        while True:
            executionResult = streamedOutput.stdout.readline()
            time.sleep(1)
            
            if executionResult:
             print(executionResult)
             self.sendOutputToQueue(executionResult)
            else:
             logging.info("End of process output")
             break

    def sendOutputToQueue(self, processOutput : str):
        print(TARGETSERVER)
        
        #queueTransport = RabbitMqReader.RabbitMqReader(TARGETSERVER, STATUSDATAQUEUE)
        self.queueManager.publish(processOutput)
        pass