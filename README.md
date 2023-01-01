# circuitpython-projects
Learning Circuit Python and Adafruit Circuit Playground Express

Install AdaFruit apps for the Circuit Playground Bluefruit

https://learn.adafruit.com/adafruit-circuit-playground-bluefruit

Download the latest version of circuitpython for the bluefruit

https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/circuitpython

Install the Bluefruit libraries on the bluefruit. Note that you don't want to install them all. Just install the individual libraries you need for specific projects because space on the Bluefruit is limited.

https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/circuit-playground-bluefruit-circuitpython-libraries

If you dowload the ZIP file you will also find example code in it.

For now, I decided to extract only the minimum adafruit circuitplayground libraries, [as specified in the documentation](https://docs.circuitpython.org/projects/circuitplayground/en/latest/#installation), into the *CIRCUITPY/lib* folder

![](./Images/extract-libraries.png)


CircuitPython documentation: https://docs.circuitpython.org/en/latest/README.html

CircuitPlayground BlueFruit library
https://docs.circuitpython.org/projects/circuitplayground/en/latest/

Download and install the MU editor

https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor

Do not use the Ubuntu Software to install it. The Mu snap is old.

From the Mu website: *On Linux, in order for Mu to work with the MicroPython based devices you need to ensure you add yourself to the correct permissions group (usually the dialout or uucp groups). Also make sure that your distribution automatically mounts flash devices, or make sure to mount them manually.*

The MU editor is available as an *appimage*. This is the first time I used an appimage

https://itsfoss.com/use-appimage-linux/

Install the appimage launcher

```bash
sudo add-apt-repository ppa:appimagelauncher-team/stable
sudo apt update
sudo apt install appimagelauncher
```

(Alternatively, install the *.deb* file available in teh AppImage Launcher Github repo at: https://github.com/TheAssassin/AppImageLauncher/releases)

Download the Mu appimage file from the downloads page. Extract the appimage file. Then double-click on it.

The appimage launcher automaticall launches and handles the installation of the appimage application and integrates it with the Ubuntu launcher. Now it shows up in a standard application search.


Open the REPL on teh BlueFruit

https://learn.adafruit.com/welcome-to-circuitpython/the-repl

https://learn.adafruit.com/adafruit-circuit-playground-express/connecting-to-the-serial-console


But, in Linux, need to [set permisisons](https://learn.adafruit.com/adafruit-circuit-playground-express/connecting-to-the-serial-console#setting-permissions-on-linux-3027345)

```
sudo adduser $USER dialout
```
And also [remove the modemmanager](https://learn.adafruit.com/adafruit-circuit-playground-express/connecting-to-the-serial-console#serial-console-issues-or-delays-on-linux-3105120)

```
sudo apt purge modemmanager
```

Restart Ubuntu (or log out and back in). This will enable the change in permissions

Start the MU editor and click on the serial butoon. You should see the REPL

![](./Images/MU-REPL.png)

Now we can start testing the CircuitPlayground using the REPL.

Turn off the eight NeoPixels around the CPB board

```
>>> import adafruit_circuitplayground
>>> adafruit_circuitplayground.bluefruit.cpb.pixels.fill(0x000000)
```

Turn the CPB LED on

```
>>> adafruit_circuitplayground.bluefruit.cpb.red_led = True
```

Make NeoPixels blink

```
>>> from adafruit_circuitplayground.bluefruit import cpb
>>> import time
>>> time.sleep(1)
>>> while True:
...     cpb.pixels.fill(0x000001)
...     time.sleep(1)
...     cpb.pixels.fill(0x000100)
...     time.sleep(1)
...     cpb.pixels.fill(0x010000)
...     time.sleep(1)
```



