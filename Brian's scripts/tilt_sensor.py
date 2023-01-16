# Code modified from https://core-electronics.com.au/guides/using-the-accelerometer-with-circuitpython-adafruit-circuit-playground-express/
import time
import board
import math
from adafruit_circuitplayground.bluefruit import cpb

pixels = cpb.pixels
pixels.brightness = 0.01

cpb.pixels.fill((0, 0, 255))
cpb.pixels.show()

while True:
    time.sleep(0.02) # slow down any printed output in the loop
    x, y, z = cpb.acceleration  # read accelerometer
    if math.fabs(x) < 3 and y > 3:
        cpb.pixels[0] = (255, 0, 0)
        cpb.pixels[9] = (255, 0, 0)
    elif x > 3 and math.fabs(y) < 3:
        cpb.pixels[6] = (255, 0, 0)
        cpb.pixels[7] = (255, 0, 0)
        cpb.pixels[8] = (255, 0, 0)
    elif math.fabs(x) < 3 and y < -3:
        cpb.pixels[4] = (255, 0, 0)
        cpb.pixels[5] = (255, 0, 0)
    elif x < -3 and math.fabs(y) < 3:
        cpb.pixels[1] = (255, 0, 0)
        cpb.pixels[2] = (255, 0, 0)
        cpb.pixels[3] = (255, 0, 0)
    else:
        cpb.pixels.fill((0, 0, 255)) 
        print("HI DAD")