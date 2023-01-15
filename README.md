# circuitpython-projects

Learning Circuit Python and Adafruit Circuit Playground Bluefruit.

## Install Circuit Python

Plug the CircuitPlayground BlueFruit into the USB port on your computer.

Install the CircuitPython and the AdaFruit apps for the [Circuit Playground Bluefruit](https://learn.adafruit.com/adafruit-circuit-playground-bluefruit). Click on the link above and follow the instructions.

First, [Install the latest version of CircuitPython](https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/circuitpython) on the Bluefruit board.

Next, install the [Bluefruit Circuit Python Libraries](https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/circuit-playground-bluefruit-circuitpython-libraries) on the board. Note that you don't want to install them all. Space on the Bluefruit is limited so just install the individual libraries you need for each project.

I decided to extract only the minimum Adafruit Circuit Playground libraries, [as specified in the documentation](https://docs.circuitpython.org/projects/circuitplayground/en/latest/#installation), into the board's *CIRCUITPY/lib* folder

I installed the following libraries:

* Folders:
  * adafruit_bus_device
  * adafruit_circuitplayground
* Files:
  * adafruit_thermistor.mpy
  * adafruit_neopixel.mpy
  * adafruit_lis3dh.mpy

![](./Images/extract-libraries.png)

For more information, read the [CircuitPython documentation](https://docs.circuitpython.org/en/latest/README.html) and the [CircuitPlayground BlueFruit library documentation](
https://docs.circuitpython.org/projects/circuitplayground/en/latest/).

## Install the MU Editor

Follow the directions in the following link to [download and install the MU editor](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor). 

> **NOTE:** **Do not** use the Ubuntu Software to install it. The MU Editor snap is out-of-date.

The MU editor is available as an [AppImage](https://itsfoss.com/use-appimage-linux/). To install the Mu Editor AppImage, first install the [AppImage Launcher](https://github.com/TheAssassin/AppImageLauncher#appimagelauncher)

```bash
sudo add-apt-repository ppa:appimagelauncher-team/stable
sudo apt update
sudo apt install appimagelauncher
```

Then, download the Mu Editor AppImage file from the [Mu website's downloads page](https://codewith.mu/en/download). Extract the AppImage file from the downloaded TAR archive. Then double-click on it.

The AppImage Launcher automatically launches and handles the installation of the application and integrates it with the Ubuntu launcher. Now it shows up in a standard application search.

Finally, [set up permissions](https://learn.adafruit.com/adafruit-circuit-playground-express/connecting-to-the-serial-console#setting-permissions-on-linux-3027345) so you can access your computer's serial port from the Mu editor. Add your userid to the *dialout* permissions group.

```bash
sudo adduser $USER dialout
```

Also, [remove the modemmanager](https://learn.adafruit.com/adafruit-circuit-playground-express/connecting-to-the-serial-console#serial-console-issues-or-delays-on-linux-3105120) package to prevent issues connecting to the serial port.

```
sudo apt purge modemmanager
```

Restart Ubuntu, or log out and back in to your user account. This will enable the change in permissions.

## Connect to the Bluefruit serial port

Start the [MU editor](https://codewith.mu/) and click on the *Serial* button. You should see the [Serial Console](https://learn.adafruit.com/adafruit-circuit-playground-express/connecting-to-the-serial-console) appear in the MU Editor's interface:

![](./Images/MU-REPL.png)

Now we can start testing the CircuitPlayground Bluefruit using the [CircuitPython REPL](https://learn.adafruit.com/welcome-to-circuitpython/the-repl). Click the *Return Key* in the Serial Console pane to start the REPL.

## Play with the LEDs

All eight Neopixels are turned off when the board was originally plugged in but they turn on when the REPL is running. They are very bright and I would like to turn them off using the REPL. 

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

Now, each of the ten Neopixels can be addressed by the index list. 

Make the first NeoPixel blink different colors:

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

> **NOTE:** The sleep statement is *required* in the While loop. If you omit the sleep statement, the board runs through the code too fast. If you have print statements in the loop, they will overload the Mu editor's serial console. Then, the Mu editor seems to get hung up and stops accepting inputs from the keyboard. Even if you restart the board to stop the loop, the Mu editor will no longer accept inputs from the keyboard. Close the Mu editor and start it again to solve this issue.

Other LEDs are available on the board. Turn the CircuitPlayground BlueFruit board's red LED on.

```python
>>> import adafruit_circuitplayground
>>> adafruit_circuitplayground.bluefruit.cpb.red_led = True
```

