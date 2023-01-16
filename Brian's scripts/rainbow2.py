import time
import math
from adafruit_circuitplayground import cp
from rainbowio import colorwheel

pix_count = 10
pixels = cp.pixels
pixels.brightness = 0.2

while True:
    for pix in range(pix_count-1,-1,-1): # backwards from pix_count to 0
        for colr in range(0,255,math.ceil(255/pix_count)): # a range of pix_count values
            pixels[pix] = (colorwheel(colr))
            pix = pix -1 
            time.sleep(0.01)
            