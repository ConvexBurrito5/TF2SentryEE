from picamera2 import Picamera2
from IO.camera import Camera
import cv2

class PiCamera(Camera):
    def __init__(self, resolution=(640,480), cap_fps=30) -> None:
        super().__init__(resolution, cap_fps)
        self.camera = Picamera2()
        config = self.camera.create_video_configuration(main={"format": 'YUV420',"size": (resolution[0], resolution[1])})
        self.camera.configure(config)
        self.camera.start()
    

    def get_frame(self) -> cv2.typing.MatLike:
        image = self.camera.capture_array()
        return image
    