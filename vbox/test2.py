import os

str = os.popen("vboxmanage showvminfo 7873f344-1417-405b-b9cc-eb974f5f2dcf --machinereadable")
print(str)