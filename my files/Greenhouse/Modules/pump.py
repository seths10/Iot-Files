from machine import Pin
import time

pump = Pin(0, Pin.OUT)


def pump_water():
    for i in range(2):
        pump.value(1)
        time.sleep(2)
        pump.value(0)
        time.sleep(2)
