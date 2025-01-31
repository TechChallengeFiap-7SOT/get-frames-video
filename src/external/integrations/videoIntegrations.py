from src.pkg.interfaces.externalInterfaces import videoExternalInterface

import requests
import subprocess

class videoIntegrations(videoExternalInterface):
    def __init__(self):
        super().__init__()

    def downloadVideo(self, videoId: str):
        #requisitar url para baixar o vdieo, de uma api externa
        videoUrl = requests.get(f'http://api.com/video/{videoId}')
        #baixar o video
        video = requests.get(videoUrl)
        videoName = "Um_nome" #Verificar se vou conseguir o nome do arquivo
        #salvar o video 
        videoPathToSave = f'./videos/{videoName}.mp4'
        with open(videoPathToSave, 'wb') as f:
            f.write(video.content)
        #retorna diretorio do arquivo do video
        return videoPathToSave #Path do vídeo que foi salvo!
        
    def getFrames(self, videoPath: str, pathToSaveFrames: str):
        command = ["ffmpeg", "-i", videoPath, "-vf", "fps=1", "{}/frame_%08d.png".format(pathToSaveFrames)]
        subprocess.call(command,shell=True)
        return pathToSaveFrames