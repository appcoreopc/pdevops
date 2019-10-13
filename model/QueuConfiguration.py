
from enum import Enum

class QueueConfiguration(Enum):
    FAN_OUT = 1
    TOPIC = 2
    DIRECT = 3

class QueuConfiguration:
    def __init__(self, queueType : QueueConfiguration, queueName : str):
        self.queueType = queueType
        self.queueName = queueName