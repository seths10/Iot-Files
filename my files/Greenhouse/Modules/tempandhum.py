from machine import Pin
import dht


dht = dht.DHT11(Pin(33))

def temp_measure():
    dht.measure()
    temp = dht.temperature()
    hum = dht.humidity()

    print("Temperature: ", str(temp))
    print("Humudity: " , str(hum))