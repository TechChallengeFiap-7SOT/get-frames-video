#Puxar da fila o vídeo
#processar o vídeo e transformar em frames
#colcoar esses frames em um zip
#apagar frames fora do zip
#Fazer upload do zip
#Apagar zip local
#Chamar a api principal


import os
import subprocess
from pathlib import Path
import shutil
import uuid
from datetime import datetime



def getFrames(videoPath, pathToSaveFrames):
    command = ["ffmpeg", "-i", videoPath, "-vf", "fps=1", "{}/frame_%08d.png".format(pathToSaveFrames)]
    subprocess.call(command,shell=True)
    return pathToSaveFrames

def createPath(pathName: str):
    diretorio = Path(pathName)
    diretorio.mkdir(parents=True, exist_ok=True)
    print(f"Diretório '{diretorio}' criado com sucesso!")
    return diretorio

def deletePathAndFiles(pathName: str): 
    diretorio = pathName
    shutil.rmtree(diretorio, ignore_errors=True)  # `ignore_errors=True` evita erros se o diretório não existir
    print(f"Diretório '{diretorio}' e seu conteúdo foram removidos!")
    return diretorio

def createZipFromPath(pathName: str, zipName: str):
    diretorio = pathName

    # Obtém o caminho absoluto do diretório do script
    diretorio_projeto = os.path.dirname(os.path.abspath(__file__))
    print(diretorio_projeto)
    zip_destino = os.path.join(diretorio_projeto, "tempZip/{}".format(zipName))
    print(zip_destino)
    shutil.make_archive(zip_destino, 'zip', diretorio)
    return zip_destino

def generateRandomPathName(videoName):

    for strings in [".mp4", "/", "."]:
        videoName = videoName.replace(strings, "")
    agora = datetime.now()
    data_str = agora.strftime("%Y%m%d%H%M%S%f")  # Remove traços, pontos e espaços
    nome_pasta = f"{videoName}_{data_str}"  # Remove hífens
    print(nome_pasta)
    return nome_pasta


video = "./telescopio.mp4"


pathName = generateRandomPathName(video)
folderPath = createPath(pathName)
framelistPath = getFrames(video, folderPath)
zipPath = createZipFromPath(framelistPath, pathName)
deletedPath = deletePathAndFiles(framelistPath)

print("Finalizado! O zip está disponível em: {}".format(zipPath))