# CircuitPython Projects

This repository contains notes and code I created while learning Circuit Python using the Adafruit Circuit Playground Bluefruit.

## Install Circuit Python

Plug the CircuitPlayground BlueFruit into the USB port on your computer.

Follow the directions in the following links to [install the CircuitPython and the AdaFruit apps](https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/circuitpython) for the Circuit Playground Bluefruit. The directions show how to [install the latest version of CircuitPython](https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/circuitpython) on the Bluefruit board and then how to [install the Bluefruit Circuit Python Libraries](https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/circuit-playground-bluefruit-circuitpython-libraries) on the board.

### Choose libraries

Space on the Bluefruit is limited so just install the specific libraries you need for each project. For now, extract the minimum Adafruit Circuit Playground libraries, [as specified in the documentation](https://docs.circuitpython.org/projects/circuitplayground/en/latest/#installation).

Install the following libraries:

* Folders:
  * adafruit_bus_device
  * adafruit_circuitplayground
* Files:
  * adafruit_thermistor.mpy
  * adafruit_neopixel.mpy
  * adafruit_lis3dh.mpy

The libraries are installed by copying library files into the board's *CIRCUITPY/lib* folder.

![Extract CircuitPython libraries](./Images/extract-libraries.png)

For more information, read the [CircuitPython documentation](https://docs.circuitpython.org/en/latest/README.html) and the [CircuitPlayground BlueFruit library documentation](
https://docs.circuitpython.org/projects/circuitplayground/en/latest/).

## Install the Mu Editor

Adafruit recommends using the [Mu editor](https://codewith.mu/) with its microcontroller boards. 

Follow the directions in the following link to [download and install the Mu editor](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor). 

> **NOTE:** **Do not** use the Ubuntu Software application to install the Mu editor because the snap in Ubuntu's software store is out-of-date.

The Mu editor is available as an [AppImage](https://itsfoss.com/use-appimage-linux/). To install the Mu Editor AppImage, first install the [AppImage Launcher](https://github.com/TheAssassin/AppImageLauncher#appimagelauncher) application.

```bash
sudo add-apt-repository ppa:appimagelauncher-team/stable
sudo apt update
sudo apt install appimagelauncher
```

Then, download the Mu Editor AppImage file from the [Mu website's downloads page](https://codewith.mu/en/download). Extract the AppImage file from the downloaded TAR archive. Then double-click on the AppImage file.

The AppImage Launcher automatically installs the application and integrates it with the Ubuntu launcher. Now it shows up in a standard application search.

Remember to [set the editor mode](https://codewith.mu/en/tutorials/1.2/modes) to *CircuitPython*.

### Fix permissions

Finally, [set up permissions](https://learn.adafruit.com/adafruit-circuit-playground-express/connecting-to-the-serial-console#setting-permissions-on-linux-3027345) so you can access your computer's serial port from the Mu editor. Add your userid to the *dialout* permissions group.

```bash
sudo adduser $USER dialout
```

Also, [remove the modemmanager package](https://learn.adafruit.com/adafruit-circuit-playground-express/connecting-to-the-serial-console#serial-console-issues-or-delays-on-linux-3105120) to prevent issues connecting to the serial port.

```
sudo apt purge modemmanager
```

Restart Ubuntu, or log out and back in to your user account. This will enable the change in permissions.

## Connect to the Bluefruit serial port

Start the Mu editor and click on the *Serial* button. You should see the [Serial Console](https://learn.adafruit.com/adafruit-circuit-playground-express/connecting-to-the-serial-console) appear in the Mu Editor's interface:

![](./Images/MU-REPL.png)

For more information, see the [Mu editor documentation regarding Adafruit boards](https://codewith.mu/en/tutorials/1.2/adafruit).

## Running code and using the REPL

Open the *code.py* file on the Bluefruit by pressing the *Load* button on the Mu editor and selecting the *code.py* file. If you are using the board for the first time, you will see a simple "Hello World" program in the *code.py* file. It prints one line of text in the serial console, then stops.

By default, the Bluefruit will automatically run changes to the *code.py* file when it is saved, so your updated code starts running as soon as you save the file.

Use the *Enter* key, *Ctrl-D*, and *Ctrl-C* to control whether the serial console is running the program stored on the board or is running code from the REPL.

* To run the *code.py* program again, press *Ctrl-D*.
* To switch to the CircuitPython REPL, press *Enter*.
* To switch from the REPL to running the *code.py* program, press *Ctrl-D*.
* If you are running a loop in the *code.py* program and want to stop it and switch to the REPL, press *Ctrl-C*, and then *Enter*.
* If you are running a loop in the REPL and want to exit the loop and return to the REPL, press *Ctrl-C*.
* If you have a REPL prompt and want to run the *code.py* program, press *Ctrl-D*.

## Play with the LEDs

Now we can start testing the CircuitPlayground Bluefruit using the [CircuitPython REPL](https://learn.adafruit.com/welcome-to-circuitpython/the-repl). Click the *Return Key* in the Serial Console pane to start the REPL.

All ten Neopixels built into the Circuit Playground Bluefruit are turned off when the board is originally plugged in but they turn on when the REPL is running. They are very bright and you may want to turn them off when using the REPL.

Turn off the ten NeoPixels around the CPB board by entering the following code into the REPL:

```python
>>> import board
>>> import neopixel
>>> pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=True)
```

The *pixels* object created by the *NeoPixel* class is a list of values representing the RGB values for each pixel. For example, list the current pixel values:

```python
>>> print(pixels)
[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
```

When you  the values, you cause the board to light up the pixels using the values in the list. The *pixel.show()* function forces the board to read the values in the *pixels* list and update the NeoPixels. Since the *pixels* list defaults to all zero values, this turns the NeoPixels off. 

```python
>>> pixels.show()
```

The *pixels.show* function is most useful if you set value of the auto_write parameter to False when you create the *pixels* object. In that case, the board will let you change the value of multiple NeoPixels but will not change the NeoPixels until you run the *pixels.show()* function.

You can decide for yourself if you want all the pixels to update every time you change any pixel value, or if you want to trigger an update separately with the show function by choosing whether the value of the *pixels* object's *auto_write* parameter is *True* or *False*. Note that the default value for *auto_write* is *True*.

After executing the statements shown above, each of the Bluefruit board's ten Neopixels can be addressed by the *pixels* list index.

For example, the first NeoPixel is addressed by the list index *0*. For example: `pixels[0]`. To demonstrate this, make the first NeoPixel blink different colors by executing the following statements in the REPL:

```python
>>> import time
>>> while True:
...     pixels[0] = (0,0,1)
...     time.sleep(1)
...     pixels[0] = (0,1,0)
...     time.sleep(1)
...     pixels[0] = (1,0,0)
...     time.sleep(1)
```

See that the first NeoPixel blinks blue, green, then red, and repeats every second.

Stop the loop by entering *CTRL-C* in the serial console.

### Sleep statement and serial console

The sleep statement is required in the While loop if you are monitoring output to the serial console.

If you omit the sleep statement, the board runs through the code too fast and print statements in the loop will overload the Mu editor's serial console. Then, the Mu editor seems to get hung up and stops accepting inputs from the keyboard. Even if you restart the board to stop the loop, the Mu editor will no longer accept inputs from the keyboard.

To solve this issue, close the Mu editor and start it again.

### Other LEDs

Other LEDs are available on the board. Turn the CircuitPlayground BlueFruit board's red LED on, then off, execute the following statements:

```python
>>> import adafruit_circuitplayground
>>> adafruit_circuitplayground.bluefruit.cpb.red_led = True
```

> **NOTE:** you may see the error message, "ValueError: NEOPIXEL in use" when you import the *adafruit_circuitplayground* library module. Fix this issue by clearing the memory. To clear the REPL memory, press *Ctrl-D*, then *Ctrl-C*, then *Enter*. Now you can start again with a blank slate.

See that the red LED is on. Then:

```python
>>> import adafruit_circuitplayground
>>> adafruit_circuitplayground.bluefruit.cpb.red_led = False
```

See that the red LED is off.

## Writing programs

If you find your experiments need more than a few lines of code, it is probably better to edit the *code.py* file on the Circuit Playground Bluefruit. See the CircuitPython documentation about [Creating and Editing Code](https://learn.adafruit.com/adafruit-circuit-playground-express/creating-and-editing-code) for more details.

In the Mu editor, load the *code.py* program and change it to the following (which is [inspired by the CircuitPython LED documentation](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino/circuitpython-internal-rgb-led#making-rainbows-because-who-doesnt-love-em-2984015)). This program will make the NeoPixels cycle through a rainbow color effect:

```python
import board
import neopixel
from rainbowio import colorwheel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2)
i = 0
while True:
    for i in range(256): # run from 0 to 255
        pixels.fill(colorwheel(i))
        print(pixels[0])
        time.sleep(0.1)
```

After pressing the Mu editor's *Save* button, the program should start to run. If it does not, click on the serial console window pane and press *Ctrl-C*, then *Ctrl-D* to exit the REPL and start the program.

The program gradually changes the value of each NeoPixel so they cycle through the colors of the rainbow. The program also outputs the color values used by the first NeoPixel to the serial console so you can see what values are changing.

To stop the program running, click on the serial console window pane and press *Ctrl-C*.

## Go mobile

After creating a program that does what you like, you may wish to carry the Bluefruit around without requiring it to be tethered to your computer. To do this, you must first eject the Bluefruit, then disconnect it from the USB port and connect it to a [battery power supply](https://www.adafruit.com/category/889).

### Eject the board

To eject the Bluefruit, close the Mu editor. Then, open the Ubuntu Files application and click on the *Eject* icon next to the *CIRCUITPY* drive. This procedure ensures you do not [corrupt the Bluefruit's file system](https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/creating-and-editing-code#editing-code-2977443).

### Battery

Connect your [battery pack](https://www.adafruit.com/product/727) to the Bluefruit using the 2-Pin JST connector. The code should start running as soon as you turn on the power. Now you can take your Bluefruit anywhere to demonstrate your cool code.

> **NOTE:** To make it easier to remove the JST connector from the board, cut off the two small tabs on the left and right sides of the battery pack's JST connector before you insert it onto the board. The tabs are very small and are easy to trim with a sharp knife.

## Experimenting with other libraries

Add new libraries when needed. Some libraries can make common operations easier. For example, if you want to create an animated display composed of different colored NeoPixels moving around the Bluefruit, you could manually operate each NeoPixel as follows:

```pixel
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
```

In this example, the [*adafruit_led_animation* library](https://docs.circuitpython.org/projects/led-animation/en/latest/api.html#adafruit-led-animation-animation-rainbowchase) will automatically create animations and has a built-in Rainbow Chase animation that will perform the same task as the code listed above, in a simpler way.

First, you need to add the new library. To add a library, open the CircuitPython archive you downloaded earlier or [download it again](https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/circuit-playground-bluefruit-circuitpython-libraries). Go to the *lib* subdirectory and extract the necessary libraries from the archive to to the Bluefruit's *CIRCUITPY/lib* directory.

```python
from adafruit_circuitplayground import cp
from adafruit_led_animation.animation.rainbowchase import RainbowChase

cp.pixels.brightness = 0.02
rainbow = RainbowChase(cp.pixels, speed=0.02, size=1, spacing=0, reverse=True, step=25)
while True:
    rainbow.animate()
```
As you can see, the *adafruit_led_animation* library creates a similar animation with less code. The led_animation library can also support much more complex configurations of NeoPixels.










