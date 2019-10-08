# docker run -d -p 5672:5672 rabbitmq
from typing import List
from time import sleep
from celery import Celery
from celery.utils.log import get_task_logger
import subprocess
from model.commandtype import CommandType

logger = get_task_logger(__name__)

app = Celery('tasks', backend='rpc://', result_persistent = True
,broker='amqp://guest:guest@localhost:5672')

app.conf.update(    
    result_serializer='json'  
)

@app.task(ignore_result=False, bind=True)
def execute(self, commands : List[CommandType]):
    # redirect_stdouts_to_logger
    try:
      logger.info("Executing", commands.title)  

      for singleProcess in commands: 
       processOutputResult = subprocess.check_output(["ls", "-l"], stdout=subprocess.PIPE, bufsize=1)

       self.update_state(state="PROGRESS", meta=processOutputResult.decode("utf-8"))
    except :
        logger.info("Error")
    return True