#!/usr/bin/env python

from registerjob.JobHandler import JobHandler
import json


def execute(ch, method, properties, body):
        data = json.loads(body, 'utf-8')
        print(" [x] Received from revieve " , data)

class recieve(JobHandler):

    def __init__(self):
        JobHandler.__init__(self, "recieve", True, True, execute)

    
