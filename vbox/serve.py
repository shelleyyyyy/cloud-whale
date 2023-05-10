from flask import Flask, request
import os
import time
import json
from flask_cors import CORS
from functools import wraps
#from pocketbase import PocketBase 

app = Flask(__name__)
#cors = CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            print(token)
        # return 401 if token is not passed
        if not token:
            return json.dumps({'message' : 'Token is missing !!'}), 401
  
        try:
            print("Check token")

            # decoding the payload to fetch the stored details
            #data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            #grab data if needed
        except:
            return json.dumps({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users contex to the routes
        return  f(*args, **kwargs)
  
    return decorated

@app.route("/")
@token_required
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/list")
@token_required
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
@token_required
def start_vm():
    print(request.json['id'])
    id = request.json['id']
    command = "vboxmanage startvm {} --type headless".format(id)
    print(command)
    os.popen(command)
    return "done"

@app.route("/stopvm", methods=['POST'])
@token_required
def stop_vm():
    print(request.json['id'])
    id = request.json['id']
    command = "vboxmanage controlvm {} poweroff".format(id)
    print(command)
    os.popen(command)
    return "done"

@app.route("/createvm", methods=['POST'])
@token_required
def create_vm():
    print(request.json)
    os_name = request.json['os']
    name = request.json['name']
    #dir_command = "mkdir /home/cole/VirtualBox\ VMs/{}".format(name)
    #os.system(dir_command)
    #os_command = "VBoxManage export {0} --output /home/cole/VirtualBox\ VMs/{1}/{2}.ova".format(os_name, name, name)
    #os.system(os_command)

    # Get the current working directory
    cwd = os.getcwd()

    # Define a relative path
    relative_path = "vms"

    # Get the absolute path
    absolute_path = os.path.abspath(os.path.join(cwd, relative_path))
    absolute_path = absolute_path.split("/vbox")[0]
    print("ABS", absolute_path)

    import_command = 'VBoxManage import {0}/vms/{1}.ova --vsys 0 --vmname "{2}"'.format(absolute_path, name, name)

    print("commmand", import_command)


    os.system(import_command)

    #boot vm once and grab IP
    command = "vboxmanage startvm {0} --type headless".format(name)
    print(command)
    os.popen(command)

    time.sleep(90)
    ip_command = "VBoxManage guestproperty enumerate {0}".format(name)
    ip = os.popen(ip_command).read()
    ip = ip.split("Name: /VirtualBox/GuestInfo/Net/0/V4/IP, value: ")[1]
    ip = ip.split(",")[0].strip()
    print(ip)

    command = "vboxmanage controlvm {0} poweroff".format(name)
    print(command)
    os.popen(command)

    #grab the new VM's ID for client
    info_command = 'VBoxManage showvminfo {}'.format(name)
    data = os.popen(info_command).read()
    data = data.split("UUID:")[1]
    data = data.split("Config file:")[0].strip()

    return json.dumps({"id": data, "ip": ip})

@app.route("/deletevm", methods=['POST'])
def delete_vm():
    print(request.json)
    name = request.json['name']
    delete_command = "VBoxManage unregistervm --delete /home/cole/VirtualBox\ VMs/{0}/{1}.vbox".format(name, name)
    os.system(delete_command)
    return "deleting"

@app.route("/info", methods=['POST'])
def get_info():
    print(request.json)
    id = request.json['id']
    info_command = "vboxmanage showvminfo {0} | grep -c 'running (since'".format(id)
    result = os.popen(info_command).read()
    result = result.strip()
    print("result", result)
    if result == '0':
        return json.dumps("off")
    return json.dumps("on")