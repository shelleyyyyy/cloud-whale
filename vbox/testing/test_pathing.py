import os

# Get the current working directory
cwd = os.getcwd()

# Define a relative path
relative_path = "vms"

# Get the absolute path
absolute_path = os.path.abspath(os.path.join(cwd, relative_path))
absolute_path = absolute_path.split("/vbox")[0]
print("ABS", absolute_path)

#name = 'LinuxLite'
#updated_name = "LinuxLite2"

import_command = 'VBoxManage import {0}/vms/{1}.ova --vsys 0 --vmname "{2}"'.format(absolute_path, name, updated_name)

print("commmand", import_command)


os.system(import_command)
