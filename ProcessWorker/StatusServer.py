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
import asyncio

import messageQueue 
from AppConstants import BUILDREQUESTQUEUE, TARGETSERVER, FAN_OUT, STATUSDATAQUEUE
from model.QueuConfiguration import QueueConfiguration, QueueType

class StatusServer:

    def __init__(self, websocket):
        self.websocket = websocket

    def execute(self, command: str) -> bool:
        print('sending data over websocket')
        #self.websocket.send(command)
    