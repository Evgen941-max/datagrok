#!/usr/bin/env python

import json, subprocess, psutil
from flask import Flask

app = Flask(__name__)

json_key={}

@app.route('/')

def general():

    def cpu_usage():
        cpu_usage = psutil.cpu_percent(interval=2)
        json_key['cpu_usage'] = float(cpu_usage)

    def volts():
        cpu_comm = "sensors | grep in0 | awk '{print $2}'"
        cpu_value = subprocess.check_output(cpu_comm, shell=True)
        json_key['volts'] = float(cpu_value.rstrip(b'\n'))

    def disk_percent():
        cmd_uptime = "df -h | grep sda5 | awk '{print $5}' | sed 's/%//g'"
        hdd_data = subprocess.check_output(cmd_uptime, shell=True)
        json_key['hdd_percent'] = float(hdd_data.rstrip(b'\n'))

    def used_memory():
        mem_used = psutil.virtual_memory()
        json_key['used_memory'] = mem_used.total >> 20

    def percent_mem():
        mem_percent = psutil.virtual_memory().percent
        json_key['percent_memory'] = mem_percent

    def print_json():
        ret = print(json.dumps(json_key))
        return json_key

    if __name__ == "__main__":
        cpu_usage()
        #volts()
        disk_percent()
        used_memory()
        percent_mem()
        print_json()

    pet = print(json.dumps(json_key))
    return json_key


if __name__ == "__main__":
    general()
    app.run(host='0.0.0.0', port=5000)