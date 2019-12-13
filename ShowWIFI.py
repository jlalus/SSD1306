import os
import subprocess
import time
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

foo = subprocess.Popen("ifconfig wlan0 | grep 'inet addr' | cut -d: -f2 | awk '$
bar ="ip:"+str(foo.read().decode())


serial = i2c(port=0, address=0x3C)
device = ssd1306(serial)
with canvas(device) as draw:
       draw.rectangle(device.bounding_box, outline="white")
       draw.text((3, 3),bar, fill="white")
time.sleep(10)