from abc import ABC, abstractmethod

class videoExternalInterface(ABC):

    @abstractmethod
    def downloadVideo(self, videoId: str):
        pass

    @abstractmethod
    def getFrames(self, videoPath: str, pathToSaveFrames: str):
        pass