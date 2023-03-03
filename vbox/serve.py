from flask import Flask, request
import os
import json
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/list")
def list_machines():
    list = os.popen('VBoxManage list vms').read()
    list = ''.join(list.splitlines())
    list = list.replace('"', '')
    list = list.split('}')

    vms = []
    for x in list:
        if x == '':
            continue
        split = x.split('{')
        vm = {
            "title": split[0],
            "id": split[1]
        }
        vms.append(vm)
    print(vms)
    return json.dumps(vms)

@app.route("/startvm", methods=['POST'])
def start_vm():
    print(request.json['id'])
    id = request.json['id']
    command = "vboxmanage startvm {} --type headless".format(id)
    print(command)
    os.popen(command)
    return "done"

@app.route("/stopvm", methods=['POST'])
def stop_vm():
    print(request.json['id'])
    id = request.json['id']
    command = "vboxmanage controlvm {} poweroff".format(id)
    print(command)
    os.popen(command)
    return "done"

    
