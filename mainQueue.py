from dotenv import load_dotenv
import os
import  boto3
import time

from src.external.integrations.videoIntegrations import videoIntegrations, videoIntegrationsMock
from src.adapters.controller.videoController import videoController

import json

import requests

load_dotenv()

my_var = os.getenv("MY_VARIABLE")

QUEUE_URL = os.getenv("QUEUE_URL")
AWS_ACCESS_KEY_ID= os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")
URL_TO_SEND_ZIP = os.getenv("URL_TO_SEND_ZIP")

sqs = boto3.client('sqs', 
            region_name='us-east-1',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            aws_session_token=AWS_SESSION_TOKEN)

videoIntegrations = videoIntegrations()
videoIntegrationsMock = videoIntegrationsMock()

def getZip(videoUrl: str):
    
    zipTah = videoController.getZipFramesFromVideo(videoUrl, videoIntegrations)

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

        url = json.loads(message['Body'])['message']['url_video']

        sqs.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=receipt_handle
        )
 
        print("Mensagem deletada.")

        zipPath = getZip(url)

        print("Segue o zip!", zipPath)

        url = URL_TO_SEND_ZIP
        print("Enviando zip para o endpoint", url)
        files = {"file": open(zipPath, "rb")}
        response = requests.post(url, files=files)

        print(response.status_code)

if __name__ == "__main__":

    #criar uma pasta chamada videos na origem
    pasta = "./videos"
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    while True:    
        receive_and_delete_message()
        # time.sleep(10) 
