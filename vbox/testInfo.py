import os

data = os.popen('VBoxManage showvminfo "LinuxLite"').read()
data = data.split("UUID:")[1]
data = data.split("Config file:")[0].strip()
print(data)