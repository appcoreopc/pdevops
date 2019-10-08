# docker run -d -p 5672:5672 rabbitmq

from time import sleep
from celery import Celery
from celery.utils.log import get_task_logger
import subprocess

logger = get_task_logger(__name__)

app = Celery('tasks', backend='rpc://', result_persistent = True
,broker='amqp://guest:guest@localhost:5672')


app.conf.update(    
    result_serializer='json'  
)

@app.task(ignore_result=False, bind=True)
def run_shell_command(self, command, args):

    # redirect_stdouts_to_logger

    outputs = subprocess.check_output([command, args])
    self.update_state(state="PROGRESS", meta=outputs.decode("utf-8"))
    return True

