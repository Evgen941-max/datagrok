#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
import json, psutil

app = Flask(__name__)

json_key={}

@app.route('/')

def percent_mem():
    mem_percent = psutil.virtual_memory().percent
    json_key['percent_mem'] = mem_percent
    return json_key

'''This function is used to retrive values used by td-agent'''
def print_json():
    ret = print(json.dumps(json_key))
    return ret

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)