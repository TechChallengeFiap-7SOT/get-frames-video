#pegar um video
#transformar em frames
#Salvar os frames 
#por td em um zip
#retornar


import os
import subprocess

command = ["ffmpeg", "-i", "video.mp4", "-vf", "fps=1", "frames/output_%04d.png"]


subprocess.call(command,shell=True)