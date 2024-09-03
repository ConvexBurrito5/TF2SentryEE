from picamera2 import Picamera2
from IO.camera import Camera
import cv2


class PiCamera(Camera):
    def __init__(self, resolution=(900, 900), cap_fps=30, original_res=(900, 900), dist_from_camera=14.8125,
                 ppi=58) -> None:
        super().__init__(resolution, cap_fps, original_res, dist_from_camera, ppi)
        self.camera = Picamera2()
        config = self.camera.create_video_configuration(
            main={"format": 'YUV420', "size": (resolution[0], resolution[1])})
        self.camera.configure(config)
        self.camera.start()

    def get_frame(self) -> cv2.typing.MatLike:
        image = self.camera.capture_array()
        return image
