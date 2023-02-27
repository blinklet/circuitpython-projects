import time 
import board 
from rainbowio import colorwheel
import neopixel

pixels = neopixel.NeoPixel(board.A2, 30, brightness=0.2, auto_write=False)

def color_chase(color, wait):
    for i in range(30):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)

def rainbow(wait):
    for j in range(255):
        for i in range(len(pixels)):
            idx = int(i + j)
            pixels[i] = colorwheel(idx & 255)
        pixels.show()
        time.sleep(wait)
    

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(30):
            rc_index = (i * 256 // 30) + j * 5
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


RED = (255,0,0)
YELLOW = (255,150,0)
GREEN = (0,255,0)
CYAN = (0,255,255)
BLUE = (0,0,255)
PURPLE = (180,0,255)
WHITE = (255,255,255)
OFF = (0,0,0,)

color_chase_demo = 0
rainbow_cycle_demo = 1
rainbow_demo = 0
flash_demo = 0

while True:
    if color_chase_demo:
        color_chase(RED, 0.1)
        color_chase(YELLOW, 0.1)
        color_chase(GREEN, 0.1)
        color_chase(CYAN, 0.1)
        color_chase(BLUE, 0.1)
        color_chase(PURPLE, 0.1)
        color_chase(OFF, 0.1)
       
    if flash_demo:
        pixels.fill(RED)
        pixels.show()
        time.sleep(1)
        pixels.fill(GREEN)
        pixels.show()
        time.sleep(1)
        pixels.fill(BLUE)
        pixels.show()
        time.sleep(1)
        pixels.fill(WHITE)
        pixels.show()
        time.sleep(1)
        
    if rainbow_cycle_demo:
        rainbow_cycle(0.05)
    if rainbow_demo:
        rainbow(0.05)