import time
import urequests
while True:
    print("enter feed,value")
    line=input()
    s=line.split()
    data=int(s[1])
    feed=s[0]
    payload={'value':data}
    response=urequests.post("https://io.adafruit.com/api/v2/<YOUR_AIO_USERNAME>/feeds/"+feed+"/data",json=payload,headers={"X-AIO-KEY":"<YOUR_AIO_KEY>"})
    print(response.json())
    response.close()
