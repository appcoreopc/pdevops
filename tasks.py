# docker run -d -p 5672:5672 rabbitmq
from typing import List
from time import sleep
from celery import Celery
from celery.utils.log import get_task_logger
import subprocess
from model.commandtype import CommandType
import json 

logger = get_task_logger(__name__)

app = Celery('tasks', backend='rpc://', result_persistent = True
,broker='amqp://guest:guest@localhost:5672')

app.conf.update(    
    result_serializer='json'  
)

@app.task(ignore_result=False, bind=True)
def execute(self, commandstrings):

    commands = json.loads(commandstrings)
    commandResultList = []

    for command in commands:
      o = CommandType(**command)
      commandResultList.append(o)
   
    # redirect_stdouts_to_logger
    for singleProcess in commandResultList: 
      logger.info("Executing")
      processOutputResult = subprocess.check_output([singleProcess.command])
      logger.info(processOutputResult.decode("utf-8"))
      
      print(processOutputResult.decode("utf-8"))
      self.update_state(state="PROGRESS", meta=processOutputResult.decode("utf-8"))
   
    return True