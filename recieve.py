
#!/usr/bin/env python
import pika
import json
from boot.config import getHost

host= getHost()

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=host))
channel = connection.channel()

channel.queue_declare(queue='hello', durable=True)

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(" [x] Received " , data['hello'])

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
