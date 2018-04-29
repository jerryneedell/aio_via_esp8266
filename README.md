# aio_via_esp8266
transmit data to aio feed via esp8266


Test ESP8266 acces to AIO before connection to feather_m0_express 

Create Feed on AIO: example: myfeed
configure ESP8266 to connect you WiFi -- see boot.py as an exmaple

edit aio.uart to set your AIO username ans AIO_KEY

copy aio_uart.py to esp8266 as main,py
ampy -p /dev/ttyUSB0 put aio_uart.py main,py

convert urequests.py to urequests.mpy for your verision of CircuitPython
Get mpy-cross from CircuitPython release link: https://github.com/adafruit/circuitpython/releases

copy urequests.mpy to esp8266
ampy -p /dev/ttyUSB0 put aio_uart.py main,py

connect to esp8266 and open terminal session to REPL then reboot (Conotrol-D) to restart main.py.

enter <feed name> <value>
myfeed  1234


open a browser toyour AIO "feeds" page and confirm taht the feed has updated.



Prepare feather_m0_express

connect USB cable to feathe_m0_express - verify that CIRCUITPY is mounted.
open a terminal session to the REPL

copy esp8266comm.py to the feather_mo_express CIRCUITPY drive.

For the am2320 demo:
install am2320 drive -- it is part of the Adafruit_CircuitPython_Library_Bundle.
The AM2320 uses I2C so you will also need the AdaFurit_Bus_Device Library - also in the "Bundle"

copy am2320_uart.py to the feather_m0_express CIRCUITPY Drive


Disconnect power from both boards:




Connect featther_mo_espress -> esp8266:
GND -> GND
TX -> RX
RX -> TX
USB -> USB  - only connect your USB cable to the feather_m0_express  - it will power both both boards

other power options are possible,


Basic communication test:

in REPL enter:
import esp8266comm

to send a vaule to the feed enter:
myfeed 4321

to reset the esp8266 enter:
reset

enter Control-C to exit theprogram on mthe feather m0_express

To send data from the am2320 - you need to creat a feed called uarttest on AIO - or modify the am2320_aio.py code to use your feedname.

Connect to the feather_m0_express REPL or reboot if connected (control-D) and enter:
import am2320_uart

your feed should once per minute.
Enter Control-C to exit
