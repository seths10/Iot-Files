from machine import Pin
import time


led = Pin(5, Pin.OUT)
led.on()

# def red():
#     red = Pin(0, Pin.OUT)
#     red.on()
#     time.sleep(10)
#     red.off()
#     
# def yellow():
#     yellow = Pin(5, Pin.OUT)
#     yellow.on()
#     time.sleep(2)
#     yellow.off()
# 
# def green():
#     green = Pin(4, Pin.OUT)
#     green.on()
#     time.sleep(10)
#     green.off()
# 
# 
# while True:
#     red()
#     yellow()
#     green()