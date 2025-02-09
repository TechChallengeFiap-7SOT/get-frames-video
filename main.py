
from src.external.integrations.videoIntegrations import videoIntegrations, videoIntegrationsMock

from src.adapters.controller.videoController import videoController

import time

import requests

videoUrl = ""

if __name__ == "__main__":

    videoIntegrations = videoIntegrations()
    videoIntegrationsMock = videoIntegrationsMock()


    zipTah = videoController.getZipFramesFromVideo(videoUrl, videoIntegrationsMock)

    # time.sleep(2)

    # deleteFile = videoController.deleteFile(zipTah)

    print("Fim do programa", zipTah)


    url = "https://feff-2804-14c-bf28-335d-4c30-8a85-ff7b-6542.ngrok-free.app/upload"
    # url = "http://127.0.0.1:5000/upload"
    files = {"file": open(zipTah, "rb")}
    response = requests.post(url, files=files)

    print(response.json())
