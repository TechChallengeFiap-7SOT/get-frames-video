from src.pkg.interfaces.gatewayInterfaces import videoGatewayInterface
from src.pkg.interfaces.externalInterfaces import videoExternalInterface

class videoGateway(videoGatewayInterface):
    def __init__(self, videoExternal: videoExternalInterface):
        super().__init__()

        self._videoExternal = videoExternal

    def getVideo(self, videoId: str):
        return self._videoExternal.downloadVideo(videoId)
    
    def getFrames(self, videoPath: str, pathToSaveFrames: str):
        return self._videoExternal.getFrames(videoPath, pathToSaveFrames)
    