class Video:
    def __init__(self, 
                 videoPath, 
                 framesPath,
                 videoName,
                 videoId):
        self._videoPath = videoPath
        self._framesPath = framesPath
        self._videoName = videoName
        self._videoId = videoId

    @property 
    def videoPath(self):
        return self._videoPath

    @videoPath.setter
    def videoPath(self, value):
        self._videoPath = value

    @property  
    def framesPath(self):
        return self._framesPath
    
    @framesPath.setter
    def framesPath(self, value):
        self._framesPath = value

    @property
    def videoName(self):
        return self._videoName
    
    @videoName.setter
    def videoName(self, value):
        self._videoName = value

    @property
    def videoId(self):
        return self._videoId
    
    @videoId.setter
    def videoId(self, value):
        self._videoId = value