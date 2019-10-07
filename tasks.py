# docker run -d -p 5672:5672 rabbitmq

from time import sleep
from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

app = Celery('tasks', backend='rpc://', result_persistent = True
,broker='amqp://guest:guest@localhost:5672')

@app.task
def add(x, y):
    logger.info("Adding %s + %s" % (x, y))
    sleep(4)
    print("executing stuff")
    return x + y

