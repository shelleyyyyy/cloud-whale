import os

os.system("VBoxManage createvm --name LinuxLiteCreated --ostype Linux_64 --register")
os.system("VBoxManage modifyvm LinuxLiteCreated --cpus 4 --memory 4096 --vram 12")
os.system("VBoxManage modifyvm LinuxLiteCreated --nic1 bridged --bridgeadapter1 eth0")
os.system('VBoxManage storagectl LinuxLiteCreated --name "SATA Controller" --add sata --bootable on')
os.system('VBoxManage storageattach LinuxLiteCreated --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium /home/cole/vdi/LiteTest/Linux-Lite-64bit.vdi')