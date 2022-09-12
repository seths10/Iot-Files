from machine import Pin
import time

def pir_sensor():
    pir_sensor = Pin(27, Pin.IN, Pin.PULL_UP)
    pir_state = pir_sensor.value()
    return pir_state
    
def button_push():
    button_push = Pin(22, Pin.IN, Pin.PULL_UP)
    btn_state = button_push.value()
    return btn_state
    
while True:
    print("PIR_SENSOR DATA: " , pir_sensor())
    print("PUSH BUTTON DATA: " , button_push())
    print(" ")
    time.sleep(5)
    
