# Created by Steven Naliwajka, https://github.com/ConvexBurrito5/TF2SentryEE
import busio
from board import SDA, SCL


class SingletonBoardFT232H(object):
    _instance = None
    i2c_bus = None

    #Creates singleton for board object
    def __new__(cls):
        #if not hasattr(cls, '_instance'):
        if cls._instance is None:
            print("Initialized: I2C Bus")
            cls._instance = super(SingletonBoardFT232H, cls).__new__(cls)
            cls._instance.i2c_bus = busio.I2C(SCL, SDA)
        else:
            #print("I2C Bus: Using existing Bus for creation")
            pass
        return cls._instance