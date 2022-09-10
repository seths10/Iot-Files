from machine import Pin,Timer
# from servo import Servo
from time import sleep

pump = Pin(27, Pin.OUT)
led = Pin(4, Pin.OUT)
# fan = Pin(2, Pin.OUT)
# s=Servo(25)


def pump_water(data):
    pump.value(1)
    sleep(2)
    pump.value(0)
    
def led1(data1):
    led.value(1)
    sleep(1)
    led.value(0)

timer = Timer(0)
timer.init(period=5000, mode=Timer.PERIODIC, callback = led1)

pumper = Timer(33)
pumper.init(period=5000, mode=Timer.PERIODIC, callback = pump_water)

# while True:
# #     pump.value(1)
# #     led.value(1)
# #     fan.value(1)
# #     time.sleep(2)
# #     pump.value(0)
# #     led.value(0)
# #     fan.value(0)
# #     time.sleep(2)
#     s.angle(90)
#     sleep(2)
#     s.angle(0)
#     sleep(2)

