import time
import board
import neopixel
from rainbowio import colorwheel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2)
i = 0
while True:
    for i in range(256): # run from 0 to 255
        pixels.fill(colorwheel(i))
        print(pixels[0])
        time.sleep(0.02)


import board
import neopixel
from adafruit_led_animation.animation.rainbowchase import RainbowChase

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2)
rainbow = RainbowChase(pixels, speed=0.02, size=1, spacing=0, reverse=True, step=25)

while True:
    rainbow.animate()