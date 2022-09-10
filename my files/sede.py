from machine import Pin,Timer
import time

pump = Pin(27, Pin.OUT)
led = Pin(4, Pin.OUT)


def pump_light(data1):
    pump.value(1)
    time.sleep(1)
    pump.value(0)
    
    if led.value() == 1:
        led.value(0)
    else:
        led.value(1)
        
pump_and_light = Timer(33)
pump_and_light.init(period=3000, mode=Timer.PERIODIC, callback = pump_light)