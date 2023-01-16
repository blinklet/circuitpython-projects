# Code coped from https://core-electronics.com.au/guides/using-the-accelerometer-with-circuitpython-adafruit-circuit-playground-express/
 
import board
import math
from adafruit_circuitplayground.bluefruit import cpb

cpb.pixels.fill((0, 0, 10))
cpb.pixels.show()

while True:
    x, y, z = cpb.acceleration  # read accelerometer
    if math.fabs(x) < 3 and y > 3:
        cpb.pixels[0] = (10, 0, 0)
        cpb.pixels[9] = (10, 0, 0)
    elif x > 3 and math.fabs(y) < 3:
        cpb.pixels[6] = (10, 0, 0)
        cpb.pixels[7] = (10, 0, 0)
        cpb.pixels[8] = (10, 0, 0)
    elif math.fabs(x) < 3 and y < -3:
        cpb.pixels[4] = (10, 0, 0)
        cpb.pixels[5] = (10, 0, 0)
    elif x < -3 and math.fabs(y) < 3:
        cpb.pixels[1] = (10, 0, 0)
        cpb.pixels[2] = (10, 0, 0)
        cpb.pixels[3] = (10, 0, 0)
    else:
        cpb.pixels.fill((0, 0, 10))
