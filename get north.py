#requires placement in luma.core examples folder TODO: fix this

from demo_opts import get_device
from luma.core.render import canvas
import time
device = get_device()

import smbus
import math

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = ((high << 8) | low)
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

bus = smbus.SMBus(0)
address = 0x1e

bus.write_byte_data(address, 0, 0x70)
bus.write_byte_data(address, 0x01, 0xa0)
bus.write_byte_data(address, 0x02, 0)

while 2>1:

    mag_xout = read_word_2c(0x03)
    mag_yout = read_word_2c(0x05)
    mag_zout = read_word_2c(0x07)

    rad_from_x0 = math.atan2(mag_xout, mag_yout)

    print (rad_from_x0)
    print ("mag_xout: ", mag_xout)
    print ("mag_yout: ", mag_yout)
    print ("mag_zout: ", mag_zout)
    time.sleep(0.1)
    with canvas(device) as draw:
        draw.line((64, 32,64 +  30*math.cos(rad_from_x0),32 + 30*math.sin(rad_from_x0)), fill="white")

