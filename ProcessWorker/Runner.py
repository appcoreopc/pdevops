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
# from messageQueue.RabbitMqWriter import RabbitMqWriter
# from AppConstants import BUILDREQUESTQUEUE, TARGETSERVER, FAN_OUT, STATUSDATAQUEUE
# from model.QueuConfiguration import QueueConfiguration, QueueType
# from messageQueue.QueueManager import QueueManager

class ProcessRunner:

    def execute(self, command: str) -> bool:
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
            else:
             logging.info("End of process output")
             break

    def sendOutputToQueue(self, processOutput : str):
        # queueTransport = RabbitMqWriter(TARGETSERVER, STATUSDATAQUEUE)
        # buildProcessRunner = ProcessRunner()
        # queueType = QueueConfiguration(FAN_OUT, STATUSDATAQUEUE)
        # queueManager = QueueManager(queueTransport, buildProcessRunner, queueType)
        # queueManager.publish(processOutput)
        pass