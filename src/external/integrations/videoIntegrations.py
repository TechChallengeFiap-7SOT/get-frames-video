from src.pkg.interfaces.externalInterfaces import videoExternalInterface

import requests
import subprocess
import shutil

from dotenv import load_dotenv
import os


load_dotenv()

URL_TO_GET_VIDEO = os.getenv("URL_TO_GET_VIDEO")

class videoIntegrations(videoExternalInterface):
    def __init__(self):
        super().__init__()

    def downloadVideo(self, videoId: str):
        #requisitar url para baixar o vdieo, de uma api externa
        # videoId = requests.get(f'videoId')
        #baixar o video
        
        request = requests.get("{}{}".format(URL_TO_GET_VIDEO,videoId)) #localhost:8080/video/s3-url/67a6aee8b6df012130001fe1
        
        videoURL = request.json()

        video = requests.get(videoURL["s3Url"]) #localhost:8080/video/s3-url/67a6aee8b6df012130001fe1

        videoName = "frames" #Verificar se vou conseguir o nome do arquivo
        #salvar o video 
        videoPathToSave = f'./videos/{videoName}.mp4'
        with open(videoPathToSave, 'wb') as f:
            f.write(video.content)
        #retorna diretorio do arquivo do video
        return videoPathToSave #Path do vídeo que foi salvo!
        
    def getFrames(self, videoPath: str, pathToSaveFrames: str):
        command = ["ffmpeg", "-i", videoPath, "-vf", "fps=1,scale=1280:-1", "{}/frame_%08d.png".format(pathToSaveFrames)]
        # subprocess.call(command,shell=True)
        subprocess.run(command)
        return pathToSaveFrames

class videoIntegrationsMock(videoExternalInterface):
    def __init__(self):
        super().__init__()

    def downloadVideo(self, videoId: str):
        #requisitar url para baixar o vdieo, de uma api externa
        originalVideoPath = "./src/external/integrations/telescopio.mp4"
        videoPathToSave = "./videos/telescopioCopia.mp4"

        shutil.copy(originalVideoPath, videoPathToSave)  # Copia o arquivo mantendo o nome original
        #retorna diretorio do arquivo do video
        return videoPathToSave #Path do vídeo que foi salvo!
        
    def getFrames(self, videoPath: str, pathToSaveFrames: str):
        command = ["ffmpeg", "-i", videoPath, "-vf", "fps=1", "{}/frame_%08d.png".format(pathToSaveFrames)]
        subprocess.call(command,shell=True)
        return pathToSaveFrames