from machine import Pin
import time

pin = Pin(0, Pin.OUT)

#Normal Morse Code
#for i in range(100):
#    pin.on()
#    time.sleep(0.5)
#    pin.off()
#    time.sleep(0.5)
    
def short():
    for i in range(3):
        pin.on()
        time.sleep(0.2)
        pin.off()
        time.sleep(0.2)
        
def long():
    for i in range(3):
        pin.on()
        time.sleep(0.5)
        pin.off()
        time.sleep(0.5)    

#SOS Morse Code
while True:
    short()
    time.sleep(0.1)
    long()
    time.sleep(0.1)
