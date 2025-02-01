
from src.external.integrations.videoIntegrations import videoIntegrations, videoIntegrationsMock

from src.adapters.controller.videoController import videoController

if __name__ == "__main__":
    videoIntegrations = videoIntegrations()
    videoIntegrationsMock = videoIntegrationsMock()

    zipTah = videoController.getZipFramesFromVideo("1", videoIntegrationsMock)

    print("Fim do programa", zipTah)