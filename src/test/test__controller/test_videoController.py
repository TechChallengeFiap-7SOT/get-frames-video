from pathlib import Path
import pytest
from unittest.mock import MagicMock
from src.adapters.controller.videoController import videoController
from src.pkg.interfaces.externalInterfaces import videoExternalInterface

class MockVideoExternal(videoExternalInterface):
    def downloadVideo(self, videoId: str):
        return "./videos/mock_video.mp4"

    def getFrames(self, videoPath: str, pathToSaveFrames: str):
        return pathToSaveFrames

@pytest.fixture
def mock_video_external():
    return MockVideoExternal()

def test_get_zip_frames_from_video(mock_video_external):
    video_url = "http://example.com/video.mp4"
    zip_path = videoController.getZipFramesFromVideo(video_url, mock_video_external)
    
    assert zip_path.endswith(".zip")
    assert "mock_video" in zip_path

def test_delete_file():
    file_path = "./videos/mock_video.mp4"
    with open(file_path, 'w') as f:
        f.write("mock content")
    
    assert videoController.deleteFile(file_path) == True
    assert not Path(file_path).exists()