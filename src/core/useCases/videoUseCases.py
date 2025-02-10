from src.core.entites.Video import Video

from src.pkg.interfaces.gatewayInterfaces import videoGatewayInterface

import os
import sys
import subprocess
from pathlib import Path
import shutil
from datetime import datetime

class VideoUseCases:
   
    @staticmethod
    def getVideo(videoId: str, videoGateway: videoGatewayInterface):
        videoPath = videoGateway.getVideo(videoId)
        return videoPath
    
    @staticmethod 
    def getFrames( videoPath: str, videoGateway: videoGatewayInterface):
        framesPathName = VideoUseCases.generatePathNameFromFile(videoPath)
        framesPathCreated = VideoUseCases.createPath(framesPathName)
        framesPath = videoGateway.getFrames(videoPath, framesPathCreated)
        return framesPath


    @staticmethod 
    def createPath(pathName: str):
        path = Path(pathName)
        path.mkdir(parents=True, exist_ok=True)
        return path
        

    @staticmethod 
    def deletePathAndFiles(pathName: str): 
        path = pathName
        try:
            shutil.rmtree(path, ignore_errors=True)  # `ignore_errors=True` evita erros se o diretório não existir
            return True
        except:
            return False
    
    @staticmethod 
    def deleteFile(filePath: str): 
        file_path = Path(filePath)
        # Verifica se o arquivo existe antes de deletar
        if file_path.exists():
            file_path.unlink()
            return True
        else:
            return False
    
    @staticmethod 
    def createZipFromPath(framesPath: str, zipName: str):
        # workDir = os.path.dirname(os.path.abspath(__file__))
        workDir = os.path.dirname(os.path.abspath(sys.argv[0]))
        # zipName = VideoUseCases.generatePathNameFromFile(framesPath)
        zipPath = os.path.join(workDir, "tempZip/{}".format(zipName))
        zipPathFinal = shutil.make_archive(zipPath, 'zip', framesPath)
        return zipPathFinal

    @staticmethod 
    def generatePathNameFromFile(path: str):
        pathName, fileType = os.path.splitext(os.path.basename(path))
        now = datetime.now()
        dateStr = now.strftime("%Y%m%d%H%M%S%f")  # Remove traços, pontos e espaços
        fileName = f"{pathName}_{dateStr}"  # Remove hífens
        return fileName

