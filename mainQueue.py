from dotenv import load_dotenv
import os
import  boto3
import time

from src.external.integrations.videoIntegrations import videoIntegrations, videoIntegrationsMock
from src.adapters.controller.videoController import videoController

import json

import requests

load_dotenv()

QUEUE_URL = os.getenv("QUEUE_URL")
AWS_ACCESS_KEY_ID= os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")
URL_TO_SEND_ZIP = os.getenv("URL_TO_SEND_ZIP")
VIDEO_API_AUTH_TOKEN = os.getenv("VIDEO_API_AUTH_TOKEN")

sqs = boto3.client('sqs', 
            region_name='us-east-1',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            aws_session_token=AWS_SESSION_TOKEN)

videoIntegrations = videoIntegrations()
videoIntegrationsMock = videoIntegrationsMock()

def getZip(videoId: str):
    
    zipTah = videoController.getZipFramesFromVideo(videoId, videoIntegrations)

    return zipTah

def receive_and_delete_message():
    response = sqs.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=5
    )
    
    messages = response.get('Messages', [])
    if not messages:
        print("Nenhuma mensagem encontrada.")
        return
    
    for message in messages:
        receipt_handle = message['ReceiptHandle']
        print(f"Recebendo mensagem: {message['Body']}")

        videoId = json.loads(message['Body'])['message']['id_video']

        sqs.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=receipt_handle
        )
 
        print("Mensagem deletada.")

        zipPath = getZip(videoId)

        print("Segue o zip!", zipPath)

        url = URL_TO_SEND_ZIP
        print("Enviando zip para o endpoint", "{}/{}".format(url,videoId))
        
        #Enviar um form data com o zip

        fileName = zipPath.split("\\")[-1]

        # files = {"zip": open(zipPath, "rb")}

        # files = {
        #     "zip": (fileName, open(zipPath, "rb"), "application/x-zip-compressed")
        # }



        headers = {
            "accept": "application/json",
            "USER": "abc@server.com",
             "Authorization Basic": VIDEO_API_AUTH_TOKEN
        }
        
        with open(zipPath, "rb") as f:
            files = {
                "zip": (fileName, f, "application/zip")  # Pode ser application/zip ou application/x-zip-compressed
            }


            print(files, headers)

            response = requests.post("{}{}".format(url,videoId), files=files, headers=headers)

        print(response.status_code)
        print(response.text)

        #deletando o zip que foi criado
        print("Deletando o zip")
        time.sleep(2)
        os.remove(zipPath)

if __name__ == "__main__":

    #criar uma pasta chamada videos na origem
    pasta = "./videos"
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    while True:    
        receive_and_delete_message()
        # time.sleep(10) 
