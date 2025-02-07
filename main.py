
from src.external.integrations.videoIntegrations import videoIntegrations, videoIntegrationsMock

from src.adapters.controller.videoController import videoController

import time

videoUrl = ""

if __name__ == "__main__":
    videoIntegrations = videoIntegrations()
    videoIntegrationsMock = videoIntegrationsMock()

    zipTah = videoController.getZipFramesFromVideo(videoUrl, videoIntegrationsMock)

    # time.sleep(2)

    # deleteFile = videoController.deleteFile(zipTah)

    print("Fim do programa", zipTah)