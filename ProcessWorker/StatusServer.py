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

class StatusServer:

    def execute(self, command: str) -> bool:
        print('writting output to websocket')
        print(command)
        pass
    