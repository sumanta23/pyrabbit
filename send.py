#!/usr/bin/env python
import pika
import json
from boot.config import getHost

key = "recieve"
host= getHost()

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=host))
channel = connection.channel()

channel.queue_declare(queue=key, durable=True)

data = {"hello":"ji"}

data = json.dumps(data)

channel.basic_publish(exchange='',
                      routing_key=key,
                      body=data,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent")
connection.close()
