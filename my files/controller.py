from machine import Pin,PWM
import time
from sht3x import SHT3X
from servo import Servo

buzz = Pin(4, Pin.OUT)
led = Pin(5, Pin.OUT)
sht = SHT3X()

 

while True:
    def buzz_long():
        led.on()
        buz = PWM(buzz, freq=9000, duty=100)
        time.sleep(0.24)
        led.off()
        buz.deinit()
        time.sleep(0.1)

    def buzz_short():
        led.on()
        buz = PWM(buzz, freq=9000, duty=100)
        time.sleep(0.08)
        led.off()
        buz.deinit()
        time.sleep(0.1)


    temp, hum = sht.getTempAndHumi()
#     temp = 51
    print("Temperature: ", temp)
    motor = Servo(0)


    if (temp > 25):
        motor.angle(0)
        print("window opened")
        time.sleep(10)
        print("window closed")
        motor.angle(180)

      
    if (temp > 50):
        i=0
        while i<3:
            for i in range(3):
                buzz_short()
            time.sleep(0.3)
            for i in range(3):
                buzz_long()
            time.sleep(0.3)
            for i in range(3):
                buzz_short()
            time.sleep(0.3)
    
    time.sleep(30)
