from src.adapters.gateway.videoGateway import VideoGateway
from src.pkg.interfaces.externalInterfaces import videoExternalInterface

from src.core.useCases.videoUseCases import VideoUseCases

class videoController():

    @staticmethod
    def getZipFramesFromVideo(videoId: str, videoExternal: videoExternalInterface):

        videoGateway = VideoGateway(videoExternal)

        videoPath = VideoUseCases.getVideo(videoId, videoGateway)

        framesListPath = VideoUseCases.getFrames(videoPath, videoGateway)

        zipName = VideoUseCases.generatePathNameFromFile(videoPath)
        zipPath = VideoUseCases.createZipFromPath(framesListPath, zipName)

        deletedFramePathStatus = VideoUseCases.deletePathAndFiles(framesListPath)
        deletedVideoPathStatus = VideoUseCases.deleteFile(videoPath)

        #Adicionar presenter e DTO

        return zipPath
    

# pathName = generateRandomPathName(video)
# folderPath = createPath(pathName)
# framelistPath = getFrames(video, folderPath)
# zipPath = createZipFromPath(framelistPath, pathName)
# deletedPath = deletePathAndFiles(framelistPath)