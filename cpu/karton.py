#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
import json, psutil

app = Flask(__name__)

json_key={}

@app.route('/')

def cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=2)
    json_key['cpu_usage'] = float(cpu_usage)
    return json_key

'''This function is used to retrive values used by td-agent'''
def print_json():
    ret = print(json.dumps(json_key))
    return ret

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)