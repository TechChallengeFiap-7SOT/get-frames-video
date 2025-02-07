import  boto3
import time


from src.external.integrations.videoIntegrations import videoIntegrations, videoIntegrationsMock
from src.adapters.controller.videoController import videoController

import json

sqs = boto3.client('sqs', region_name='us-east-1')
queue_url = '' 
videoIntegrations = videoIntegrations()
videoIntegrationsMock = videoIntegrationsMock()

def getZip(videoUrl: str):
    
    zipTah = videoController.getZipFramesFromVideo(videoUrl, videoIntegrations)

    return zipTah

def receive_and_delete_message():
    response = sqs.receive_message(
        QueueUrl=queue_url,
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

        # sqs.delete_message(
        #     QueueUrl=queue_url,
        #     ReceiptHandle=receipt_handle
        # )
 
        # print("Mensagem deletada.")

        print("Segue o zip!", getZip(url))

if __name__ == "__main__":
    while True:    
        receive_and_delete_message()
        time.sleep(10) 
