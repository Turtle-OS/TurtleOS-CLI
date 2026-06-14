import os
import subprocess
import socket
import requests as rq

DIR = "/mnt/tcli"

os.mkdir(DIR)

# -----------------------
#       Shell.           
# -----------------------

print("TurtleOS 0.1 CLI")
print("Esta é uma versão experimental e não nos responsabilizamos por quaisquer consequências.")
while True:
    cmd = input("turtle@cli> ")
    os.system(cmd)
