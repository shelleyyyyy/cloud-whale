from flask import Flask, request
import os
import json
from functools import wraps

app = Flask(__name__)

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
    dir_command = "mkdir /home/cole/VirtualBox\ VMs/{}".format(name)
    os.system(dir_command)
    os_command = "VBoxManage export {0} --output /home/cole/VirtualBox\ VMs/{1}/{2}.ova".format(os_name, name, name)
    os.system(os_command)
    import_command = 'VBoxManage import /home/cole/VirtualBox\ VMs/{0}/{1}.ova --vsys 0 --vmname "{2}"'.format(name, name, name)
    os.system(import_command)
    return "creating"

    
