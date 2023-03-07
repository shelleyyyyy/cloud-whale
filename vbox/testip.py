import os
import time


name = "LinuxLiteShelley"

# info_command = 'VBoxManage showvminfo {}'.format(name)
# data = os.popen(info_command).read()
# data = data.split("UUID:")[1]
# data = data.split("Config file:")[0].strip()

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

#10.4.9.21

