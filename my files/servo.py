# from machine import Pin, PWM
# import time
# import uasyncio
# from servo import Servo
# 
# s = Servo(32)
# 
# #servo=PWM(Pin(32),freq=50)
# 
# 
# # servo.duty(10)
# #     servo.duty(20)
# # try:
# #     print(servo.angle())
# # except:
#     
# for i in range(10):
#     s.angle(90)
#     time.sleep(1)
#     s.angle(210)
# 
# 
#

from machine import Pin
import time
from servo import Servo

s =  Servo(25)
while True:
    s.angle(100)
    time.sleep(2)
    s.angle(0)
    time.sleep(1)
#  
#  
#

 
 
 
 
 
 
 
 
 
