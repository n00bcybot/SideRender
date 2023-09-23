import subprocess, sys

p = subprocess.Popen(["powershell.exe", "(Get-Process mayapy).HasExited"], stdout=sys.stdout)
p.communicate()

