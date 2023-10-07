import subprocess
import os
import maya.standalone
import maya.cmds as cmds

pid = 18740
process = subprocess.Popen(['mayapy', '-i'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, preexec_fn=lambda: os.setpgid(0, pid))

commands = [
    "cmds.file('C:\\Users\\fresh\\Desktop\\maya\\rendertest\\test.ma', o=True)"
    "cameras_list = cmds.listCameras()"
    "print(cameras_list)"
]

for command in commands:
    process.stdin.write(command + "\n")
    process.stdin.flush()

responce = process.stdout.readline()
print(responce)

process.stdin.close()
process.wait()



