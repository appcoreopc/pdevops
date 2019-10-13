from enum import Enum

class QueueType(Enum):
    FAN_OUT = 1
    TOPIC = 2
    DIRECT = 3

class QueueConfiguration:
    def __init__(self, queueType : QueueType, queueName : str, routingKey : str = ""):
        self.queueType = queueType
        self.queueName = queueName
        self.routingKey = routingKey