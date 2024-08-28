from IO.soundcontroller import SoundController
from playsound import playsound
import os

class SoundControllerFT232H(SoundController):

    def __init__(self):
        current_file_path = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file_path)
        try:
            self.sentry_scan_path = os.path.join(current_dir, "../../Universal/SoundFiles", "Sentry_scan.wav")
            self.sentry_spot_path = os.path.join(current_dir, "../../Universal/SoundFiles", "Sentry_spot_client.wav")
            print("Initialized: Sound Controller")
        except:
            print("Sound Controller: Audio Path is incorrect")

    def play_idle_beeping(self):
        playsound(self.sentry_scan_path)

    def play_target_spotted(self):
        #This plays "spotted" sound when called
        playsound(self.sentry_spot_path)
