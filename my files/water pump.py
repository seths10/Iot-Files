from machine import Pin
import time


pump = Pin(0, Pin.OUT)

while True:
    pump.value(1)
    time.sleep(5)
    pump.value(0)
    time.sleep(5)
