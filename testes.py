import requests

video = ""
#Baixar esse video

video = requests.get(video)

videoName = "Um_nome2" #Verificar se vou conseguir o nome do arquivo

#salvar o video

videoPathToSave = f'./videos/{videoName}.mp4'

with open(videoPathToSave, 'wb') as f:
    f.write(video.content)

#retorna diretorio do arquivo do video
