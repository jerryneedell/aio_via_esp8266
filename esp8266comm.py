import board
import busio
import time

RX = board.RX
TX = board.TX

with  busio.UART(TX, RX, baudrate=115200, timeout=3000) as uart:
    while True:
        data=input()
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





