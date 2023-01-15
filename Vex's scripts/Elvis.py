# save as "code.py"

import time
import board
from adafruit_circuitplayground import cp

is_a1_touched = cp.touch_A1

if is_a1_touched:
    print("The beginning")
is_a2_touched = cp.touch_A2
is_a3_touched = cp.touch_A3
is_a4_touched = cp.touch_A4

print("who is stayin' alive:")
print(cp.touch_pins)


while True:

    current_touched = cp.touched


    if current_touched:
        print("Houstan we have a problem in ")
        print(current_touched)
    else:
        print("Elvis has left the building.")
    if all(pad in current_touched for pad in (board.A2, board.A3, board.A4)):
        print("You have triggered the collapse of society.")
        print("Humans die out in a massive plague named 'NomoreFreeWifi-19'.")
        print("Mutant hotdogs now reign as the dominant species. Was it worth it?")
    time.sleep(0.25)