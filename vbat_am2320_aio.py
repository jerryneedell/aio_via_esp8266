import board
import busio
import time
import adafruit_am2320
import analogio



def get_voltage(pin):
    return (pin.value * 3.3) / 65536 * 2

def send_data(data):
    uart.write(data+"\n"+"\r")
    getresponse = True
    while getresponse:
        response=uart.readline()
        print(response)
        if(response==b''):
            getresponse=False



RX = board.RX
TX = board.TX
i2c = busio.I2C(board.SCL, board.SDA)
am = adafruit_am2320.AM2320(i2c)
vbat_voltage = analogio.AnalogIn(board.D9)

with  busio.UART(TX, RX, baudrate=115200, timeout=3000) as uart:
    while True:
        try:
            battery_voltage = get_voltage(vbat_voltage)
            data="vbat " + str(int(battery_voltage*1000))
            send_data(data)
            data="am2320 " + str(int(am.temperature*10))
            send_data(data)
        except OSError as e:
            print("OSError;",e)
            pass
        except RuntimeError as e:
            print("RTError;",e)
            pass
        time.sleep(60)




