
#!/usr/bin/env python
import pika
import json
from boot.config import getHost



class JobHandler():
    """
    Parent Class for all JobHandlers
    """
    
    def __init__(self, queueName, durable, no_ack, callback):
        self.initialize(queueName, durable, no_ack, callback)
    

    def initialize(self, queueName, durable, no_ack, callback):
        host= getHost()
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        channel = connection.channel()

        channel.queue_declare(queue=queueName, durable=durable)
        channel.basic_consume(callback, queue=queueName, no_ack=no_ack)

        print(' [*] Waiting for messages... ')
        channel.start_consuming() 


    
