import time
import math
from adafruit_circuitplayground import cp
from rainbowio import colorwheel


pixels = cp.pixels
pixels.brightness = 0.2
# pixels.auto_write = False
pix_count = len(pixels)

while True:
    for pix in range(pix_count-1,-1,-1): # backwards from pix_count to 0
        for colr in range(0,255,math.ceil(255/pix_count)): # a range of pix_count values
            pixels[pix] = (colorwheel(colr))
            pix = pix -1 
            time.sleep(0.01)
            # pixels.show()

# try reversing the nesting of the for loops
# then uncomment the pixels.autowrite line and the pixels.show line
