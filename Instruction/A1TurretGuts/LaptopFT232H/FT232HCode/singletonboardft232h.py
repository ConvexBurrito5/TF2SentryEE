import busio
from board import SDA, SCL


class SingletonBoardFT232H(object):
    _instance = None
    i2c_bus = None

    #Creates singleton for board object
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls._instance = super(SingletonBoardFT232H, cls).__new__(cls)
            cls._instance.i2c_bus = busio.I2C(SCL, SDA)
        return cls._instance
