#!/usr/bin/env python

from registerjob.JobHandler import JobHandler
import json


def execute(ch, method, properties, body):
        data = json.loads(body, 'utf-8')
        print(" [x] Received from sumanta " , data)

class sumanta(JobHandler):

    def __init__(self):
        JobHandler.__init__(self, "sumanta", True, True, execute)

    
