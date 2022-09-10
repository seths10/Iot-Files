import dht
from machine import Pin,PWM
import time

E = 2637
F = 2794

d = dht.DHT11(Pin(22))
buzz = Pin(0, Pin.OUT)
pir_sensor = Pin(22, Pin.IN, Pin.PULL_UP)

while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    print("Temperature: " + str(temp) + "  Humidity: " + str(hum))
    time.sleep(2)
    
    if temp >= 30:       
        buz = PWM(buzz, freq=E, duty=100)
        time.sleep(0.08)
        pin.off()
        buz.deinit()
        time.sleep(0.1)
        
        
#     pir_state = pir_sensor.value()
#     if pir_state == 1:
#         buz = PWM(buzz, freq=F, duty=100)
#         time.sleep(0.08)
#         buz.off()
#         buz.deinit()
#         time.sleep(0.1)