from IO.soundcontroller import SoundController
from playsound import playsound
import os

class SoundControllerFT232H(SoundController):

    def __init__(self):
        current_file_path = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file_path)
        parent_dir = os.path.dirname(current_dir)
        self.sentry_scan_path = os.path.join(parent_dir, "SoundFiles", "Sentry_scan.wav")
        self.sentry_spot_path = os.path.join(parent_dir, "SoundFiles", "Sentry_spot_client.wav")
        pass

    def play_idle_beeping(self):
        playsound(self.sentry_scan_path)

    def play_target_spotted(self):
        playsound(self.sentry_spot_path)