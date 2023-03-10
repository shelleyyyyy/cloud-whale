import os

os.system("mkdir /home/cole/VirtualBox\ VMs/LinuxLiteClone")
os.system("VBoxManage export LinuxLite --output /home/cole/VirtualBox\ VMs/LinuxLiteClone/LinuxLiteClone.ova")
os.system("VBoxManage import /home/cole/VirtualBox\ VMs/LinuxLiteClone/LinuxLiteClone.ova")