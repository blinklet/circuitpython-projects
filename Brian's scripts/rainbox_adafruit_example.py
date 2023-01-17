# From https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/main/examples/neopixel_rainbowio_simpletest.py
# SPDX-FileCopyrightText: 2022 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
from rainbowio import colorwheel
import neopixel

NUMPIXELS = 12  # Update this to match the number of LEDs.
SPEED = 0.05  # Increase to slow down the rainbow. Decrease to speed it up.
BRIGHTNESS = 0.2  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
PIN = board.A3  # This is the default pin on the 5x5 NeoPixel Grid BFF.

pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)


# def rainbow_cycle(wait):
#     for color in range(255):
#         for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
#             pixel_index = (pixel * 256 // len(pixels)) + color * 5
#             pixels[pixel] = colorwheel(pixel_index & 255)
#         pixels.show()
#         time.sleep(wait)

def rainbow_cycle(wait):
    for color in range(255):
        for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
            pixel_index = (pixel * 256 // len(pixels)) + color * 5
            pixels[pixel] = colorwheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


while True:
    rainbow_cycle(SPEED)

# Example
# for pixel 0, color 1
#     0 * 256 // 10 = 0, + 1 * 5 = 5, 
#     5 & 255 = 5
# for pixel 9, color 1
#     9 * 256 // 10 = 230, + 1 * 5 =  235,  1275 + 230 = 1505
#     235 & 255 = 235     
#     9 * 256 // 10 = 230, + 255 * 5 =  1275,  1275 + 230 = 1505
#     1505 & 255 = 225
