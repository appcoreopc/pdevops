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

print(dir(app))

print('logger dr')
print(dir(logger.log))


@app.task(ignore_result=False, bind=True)
def add(self, x, y):

    # redirect_stdouts_to_logger

    logger.info("Adding %s + %s" % (x, y))
    sleep(4)
    print("executing stuff")

    a = subprocess.check_output(["ls", "-l"])
    self.update_state(state="PROGRESS", meta=a.decode("utf-8"))

    print(a)
    

    return x + y

