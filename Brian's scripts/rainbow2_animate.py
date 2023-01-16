# For library information, see:
# https://docs.circuitpython.org/projects/led-animation/en/latest/api.html#adafruit-led-animation-animation-rainbowchase
from adafruit_circuitplayground import cp
from adafruit_led_animation.animation.rainbowchase import RainbowChase

cp.pixels.brightness = 0.02
rainbow = RainbowChase(cp.pixels, speed=0.02, size=1, spacing=0, reverse=True, step=25)
while True:
    rainbow.animate()