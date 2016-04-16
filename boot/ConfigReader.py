import json
import os
import codecs

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "../config.json"
abs_file_path = os.path.join(script_dir, rel_path)

config = {}

def read():
    with open('config.json') as data_file:    
        config = json.load(data_file)
    return config;

