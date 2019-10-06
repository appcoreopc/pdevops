# docker run -d -p 5672:5672 rabbitmq
from time import sleep
from celery import Celery

app = Celery('tasks', broker='amqp://guest:guest@localhost:5672')


@app.task
def add(x, y):
    sleep(4)
    print("executing stuff")
    return x + y

