import board
import neopixel
from adafruit_led_animation.animation.rainbowchase import RainbowChase

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2)
rainbow = RainbowChase(pixels, speed=0.02, size=1, spacing=0, reverse=True, step=25)

while True:
    rainbow.animate()