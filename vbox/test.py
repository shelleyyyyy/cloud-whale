import os

os.system('VBoxManage createvm --name LinuxLiteTest --ostype Debian_64 --register')
str = os.popen('VBoxManage list vms').read()
print("Printted", str)
os.system('VBoxManage modifyvm LinuxLiteTest --cpus 2 --memory 4096 --vram 12')

os.system('VBoxManage createhd --filename /home/cole/vdi/LinuxLite64bit.vdi --size 5120 --variant Standard')
os.system('VBoxManage storagectl LinuxLiteTest --name "SATA Controller" --add sata --bootable on')
os.system('VBoxManage storageattach LinuxLiteTest --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium /home/cole/vdi/LinuxLite64bit.vdi')