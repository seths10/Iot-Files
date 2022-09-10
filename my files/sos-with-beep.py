from machine import Pin,PWM
import time

buzz = Pin(0, Pin.OUT)
pin = Pin(4, Pin.OUT)

def buzz_long():
    pin.on()
    buz = PWM(buzz, freq=9000, duty=100)
    time.sleep(0.24)
    pin.off()
    buz.deinit()
    time.sleep(0.1)

def buzz_short():
    pin.on()
    buz = PWM(buzz, freq=9000, duty=100)
    time.sleep(0.08)
    pin.off()
    buz.deinit()
    time.sleep(0.1)
    

while True:
    for i in range(3):
        buzz_short()
    time.sleep(0.3)
    for i in range(3):
        buzz_long()
    time.sleep(0.3)
    for i in range(3):
        buzz_short()
    time.sleep(0.3)
    
