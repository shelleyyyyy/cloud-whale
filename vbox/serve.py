from flask import Flask
import virtualbox
vbox = virtualbox.VirtualBox()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("create")
def create_machine():
    session = virtualbox.Session()
    machine = vbox.find_machine("windows")
    # progress = machine.launch_vm_process(session, "gui", "")
    # For virtualbox API 6_1 and above (VirtualBox 6.1.2+), use the following:
    progress = machine.launch_vm_process(session, "gui", [])
    progress.wait_for_completion()
