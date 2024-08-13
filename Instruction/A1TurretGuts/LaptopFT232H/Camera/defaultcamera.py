import cv2
from IO.camera import Camera

class DefaultCamera(Camera):
    def __init__(self, resolution=(900,900), cap_fps=30, original_res=(900,900), dist_from_camera=14.8125, ppi=58) -> None:
        super().__init__(resolution, cap_fps, original_res, dist_from_camera, ppi)

        # Dont worry about resizing image because
        # we're getting the correct res from the source.
        self.cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.RESOLUTION[0])
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.RESOLUTION[1])
        self.cap.set(cv2.CAP_PROP_FPS, self.CAPTURE_FPS)
        # IT IS VERY VERY IMPORTANT THAT IT'S YU12
        # the camera will give bad image if not configured this way.
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('I', '4', '2', '0'))


    def get_frame(self) -> cv2.typing.MatLike:
        """
        Returns the frame that the camera is currently reading.
        returns img:MatLike row,col,BGR
        """
        ret_val, img = self.cap.read()
        if ret_val:
            return img
        else:
            print("frame was unable to be read...")
