
from src.external.integrations.videoIntegrations import videoIntegrations, videoIntegrationsMock

from src.adapters.controller.videoController import videoController

import time

videoUrl = "https://s3.amazonaws.com/br.com.fiap.soat7.grupo18.videoapi.uploads/abc%40server.com/sample-video.mp4-20250205224255853?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQD8erHj1gGTqyEQy4Sb1SgdrW6pHHn5Gt%2ByYF2cDaQkmgIhAPuiBTWZXsCFTZfrfyAT9bRneK5zFgRcr%2FrRkF7axlEPKqsCCFMQAhoMMjY0ODc2NTEzMzM5IgxOO1kYZy1psw7DIrIqiAJ2sQZHJrJrVlInWR1ZS%2BaVeioLDjcuFmCo2gdVZf5iQs2RdvYrtHj%2BG22%2BXxGv4XdheRQDl1fePUpDjGlIS4BWgHJ%2BK4aFibPshPThFWX11%2FMuMmKXg%2BQMIO4wXxrcHGzqzKIHAGEnvmFMpqCsBt8hdcJj%2FbO4Kcen1Ej6jm6n023RkPMpTkJ7JX11nelW3D0KlXrmXWLV5j1Z2gbW6kOta5UfWGz68pRlD2BD7ezzuLKejTnxnTAS019aICs9oMX0q4xxtQvQDbPYlDnTIe8LL6XfgVai%2F%2F%2BmdjovK25NyKoalPUeQczlwWnreDLvAQdmiipPik81%2FcuTsxNcvUwhZIBMRoa0Km0wzZ2QvQY6nAHn4HvpeVdosVIK7pTfbX6864AGwBD9XxLOEo%2F%2B7DN94EinrTBTRucpMMK4W54uRW2420yCk0oil9F7VkEIBO092RIkWwVC7EIOx%2F9XPPAH%2BoRT0GqlEqxAocTPSY57okjfp76jMXxl0MYPsw1rHsF1DmKVyuz%2BgaSLAcQn6qUSama%2BhoPzzp4LPSrGtIg8jtNimDeU6MA1pWOy%2FZ0%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250206T014301Z&X-Amz-SignedHeaders=host&X-Amz-Credential=ASIAT3K663A5ZWBDJUU6%2F20250206%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Expires=7200&X-Amz-Signature=bffc789153a15819edca1f46dc9a0d46ed7261f52a0e0e8a5c142031fd14db29"

if __name__ == "__main__":
    videoIntegrations = videoIntegrations()
    videoIntegrationsMock = videoIntegrationsMock()

    zipTah = videoController.getZipFramesFromVideo(videoUrl, videoIntegrations)

    # time.sleep(2)

    # deleteFile = videoController.deleteFile(zipTah)

    print("Fim do programa", zipTah)