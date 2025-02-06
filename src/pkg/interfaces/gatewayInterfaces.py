from abc import ABC, abstractmethod

class videoGatewayInterface(ABC):
    @abstractmethod
    def getVideo(self, videoUrl: str):
        pass

    @abstractmethod
    def getFrames(self, videoPath: str, pathToSaveFrames: str):
        pass