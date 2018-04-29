import board
import busio
import time
import adafruit_am2320

RX = board.RX
TX = board.TX
i2c = busio.I2C(board.SCL, board.SDA)
am = adafruit_am2320.AM2320(i2c)

with  busio.UART(TX, RX, baudrate=115200, timeout=3000) as uart:
    while True:
        try:
            data="uarttest " + str(int(am.temperature))
        except OSError as e:
            print("OSError;",e)
            # These sensors are a bit flakey, its ok if the readings fail
            pass
        except RuntimeError as e:
            print("RTError;",e)
            pass
        if "reset" in data:
            uart.write("\x03")
            uart.write("\x04")
        else:
            uart.write(data+"\n"+"\r")
        getresponse = True
        while getresponse:
            response=uart.readline()
            print(response)
            if(response==b''):
                getresponse=False
        time.sleep(60)




