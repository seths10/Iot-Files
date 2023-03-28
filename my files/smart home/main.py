import machine
from machine import Pin
from machine import ADC
import usocket as socket
import time
import network
import dht

# Output Pin Declaration 
FAN1 = machine.Pin(26, machine.Pin.OUT)
FAN1.value(1)

FAN2 = machine.Pin(22, machine.Pin.OUT)
FAN2.on()

FAN3 = machine.Pin(5, machine.Pin.OUT)
FAN3.value(0)

pump = machine.Pin(25, machine.Pin.OUT)
mq4 = ADC(Pin(32))
servo = machine.Pin(27, machine.Pin.OUT)
dhtPin = machine.Pin(4, machine.Pin.IN)

LED1 = machine.Pin(21,machine.Pin.OUT)
LED1.value(0)

LED2 = machine.Pin(18,machine.Pin.OUT)
LED2.value(0)

LED3 = machine.Pin(23,machine.Pin.OUT)
LED3.value(0)

LED4 = machine.Pin(32,machine.Pin.OUT)
LED4.value(0)

timeout = 0

temp = dht.DHT11(dhtPin)
wifi = network.WLAN(network.AP_IF)

# Restarting WiFi
wifi.active(False)
time.sleep(0.5)
wifi.active(True)
wifi.config(essid='SmartHome',password='11111111', authmode=network.AUTH_WPA_WPA2_PSK)

# wifi.connect('Billllll','11111111')

# if not wifi.isconnected():
#     print('connecting..')
#     while (not wifi.isconnected() and timeout < 10):
#         print(10 - timeout)
#         timeout = timeout + 1
#         time.sleep(1)
        
# if(wifi.isconnected()):
#     print('Connected...')
print('Access point available...')
print('network config:', wifi.ifconfig())
    
# HTML Document

html='''<!DOCTYPE html>
<html style="background-color: #a3abdf; color: white; font-family: 'verdana'">
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>
  <body>
    <center>
      <h2>Smart Home Control</h2>
    </center>
    <form>
      <center>
        <center><h2>Lights</h2></center>
        <div style="display: flex; flex-direction: column">
          <div
            style="
              display: flex;
              align-items: center;
              justify-content: center;
              padding: 8px;
              gap: 80px;
              border-radius: 10px;
              margin: 8px;
              margin-bottom: 20px;
            "
          >
            <div>
              <div
                style="
                  padding: 10px;
                  background-color: white;
                  border-radius: 12px;
                  color: #4a4e69;
                  margin-bottom: 30px;
                "
              >
                <h3>ROOM 1</h3>
                <button
                  name="LED1"
                  style="
                    background-color: gray;
                    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2),
                      0 6px 20px 0 rgba(0, 0, 0, 0.19);
                    color: white;
                    border-radius: 1.2rem;
                    border: 16px;
                    margin-bottom: 8px;
                    padding: 8px 20px;
                  "
                  value="ON"
                  type="submit"
                >
                  OFF
                </button>
                <button
                  name="LED1"
                  style="
                    background-color: green;
                    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2),
                      0 6px 20px 0 rgba(0, 0, 0, 0.19);
                    color: white;
                    border-radius: 1.2rem;
                    border: 16px;
                    padding: 8px 20px;
                  "
                  value="OFF"
                  type="submit"
                >
                  ON
                </button>
              </div>
              <div
                style="
                  padding: 10px;
                  background-color: white;
                  border-radius: 12px;
                  color: #4a4e69;
                "
              >
                <h3>ROOM 2</h3>
                <button
                  name="LED2"
                  style="
                    background-color: gray;
                    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2),
                      0 6px 20px 0 rgba(0, 0, 0, 0.19);
                    color: white;
                    border-radius: 1.2rem;
                    margin-bottom: 8px;
                    border: 16px;
                    padding: 8px 20px;
                  "
                  value="ON"
                  type="submit"
                >
                  OFF
                </button>
                <button
                  name="LED2"
                  style="
                    background-color: green;
                    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2),
                      0 6px 20px 0 rgba(0, 0, 0, 0.19);
                    color: white;
                    border-radius: 1.2rem;
                    border: 16px;
                    padding: 8px 20px;
                  "
                  value="OFF"
                  type="submit"
                >
                  ON
                </button>
              </div>
            </div>
            <div>
              <div
                style="
                  padding: 10px;
                  margin-bottom: 30px;
                  background-color: white;
                  border-radius: 12px;
                  color: #4a4e69;
                "
              >
                <h3>ROOM 3</h3>
                <button
                  name="LED3"
                  style="
                    background-color: gray;
                    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2),
                      0 6px 20px 0 rgba(0, 0, 0, 0.19);
                    color: white;
                    border-radius: 1.2rem;
                    margin-bottom: 8px;
                    border: 16px;
                    padding: 8px 20px;
                  "
                  value="ON"
                  type="submit"
                >
                  OFF
                </button>
                <button
                  name="LED3"
                  style="
                    background-color: green;
                    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2),
                      0 6px 20px 0 rgba(0, 0, 0, 0.19);
                    color: white;
                    border-radius: 1.2rem;
                    border: 16px;
                    padding: 8px 20px;
                  "
                  value="OFF"
                  type="submit"
                >
                  ON
                </button>
              </div>
              <div
                style="
                  padding: 10px;
                  background-color: white;
                  border-radius: 12px;
                  color: #4a4e69;
                "
              >
                <h3>ROOM 4</h3>
                <button
                  name="LED4"
                  style="
                    background-color: gray;
                    margin-bottom: 8px;
                    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2),
                      0 6px 20px 0 rgba(0, 0, 0, 0.19);
                    color: white;
                    border-radius: 1.2rem;
                    border: 16px;
                    padding: 8px 20px;
                  "
                  value="ON"
                  type="submit"
                >
                  OFF
                </button>
                <button
                  name="LED4"
                  style="
                    background-color: green;
                    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2),
                      0 6px 20px 0 rgba(0, 0, 0, 0.19);
                    color: white;
                    border-radius: 1.2rem;
                    border: 16px;
                    padding: 8px 20px;
                  "
                  value="OFF"
                  type="submit"
                >
                  ON
                </button>
              </div>
            </div>
          </div>

          <center><h2>Fans</h2></center>
          <div
            style="
              display: flex;
              justify-content: center;
              gap: 15px;
              padding: 0px;
              border-radius: 10px;
              margin: 0px 8px;
            "
          >
            <div
              style="
                padding: 10px;
                background-color: white;
                border-radius: 12px;
                color: #4a4e69;
              "
            >
              <h3>ROOM 1</h3>
              <button
                name="FAN1"
                style="
                  background-color: gray;
                  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2),
                    0 6px 20px 0 rgba(0, 0, 0, 0.19);
                  color: white;
                  border-radius: 1.2rem;
                  border: 16px;
                  padding: 8px 20px;
                "
                value="ON"
                type="submit"
              >
                OFF
              </button>
              <button
                name="FAN1"
                style="
                  background-color: green;
                  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2),
                    0 6px 20px 0 rgba(0, 0, 0, 0.19);
                  color: white;
                  border-radius: 1.2rem;
                  border: 16px;
                  padding: 8px 20px;
                "
                value="OFF"
                type="submit"
              >
                ON
              </button>
            </div>
            <div
              style="
                padding: 10px;
                background-color: white;
                border-radius: 12px;
                color: #4a4e69;
              "
            >
              <h3>ROOM 2</h3>
              <button
                name="FAN2"
                style="
                  background-color: gray;
                  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2),
                    0 6px 20px 0 rgba(0, 0, 0, 0.19);
                  color: white;
                  border-radius: 1.2rem;
                  border: 16px;
                  padding: 8px 20px;
                "
                value="ON"
                type="submit"
              >
                OFF
              </button>
              <button
                name="FAN2"
                style="
                  background-color: green;
                  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2),
                    0 6px 20px 0 rgba(0, 0, 0, 0.19);
                  color: white;
                  border-radius: 1.2rem;
                  border: 16px;
                  padding: 8px 20px;
                "
                value="OFF"
                type="submit"
              >
                ON
              </button>
            </div>
          </div>
        </div>
      </center>
    </form>
  </body>
</html>
'''

# Initialising Socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET - Internet Socket, SOCK_STREAM - TCP protocol

Host = '' # Empty means, it will allow all IP address to connect
Port = 80 # HTTP port
s.bind(('',80)) # Host,Port

s.listen(5) # It will handle maximum 5 clients at a time

def senseSmoke():
    return mq4.read()

#pumpwater 
def pumpWater():
    on(pump)
    sleep(3)
    off(pump)
    sleep(2)
    
def readTempHumid():
    try:
        time.sleep(0.5)
        value = senseSmoke()
        temp.measure()
        temperature = temp.temperature()
        humidity = temp.humidity()    
        print('Temperature=', temperature, 'C', 'Humidity=', humidity, '%')
        return temperature, humidity
    except OSError as e:
        print('Failed to read sensor.')
        
def kitchen():
    try:
        value=senseSmoke()
#         print("1.2")
        if value > 4500:
            pumpWater()
    except Exception as e:
        print(e)
        with open('error_log.txt', 'a') as err_log:
            err_log.write(str(e)+'\n')

# main loop
while True:  
  connection_socket,address=s.accept() # Storing Conn_socket & address of new client connected
  print("Got a connection from ", address)
  request=connection_socket.recv(1024) # Storing Response coming from client
  print("Content ", request) # Printing Response 
  request=str(request)# Coverting Bytes to String
  
  # Comparing & Finding Postion of word in String 
  LED1_ON =request.find('/?LED1=ON')
  LED1_OFF =request.find('/?LED1=OFF')
  
  LED2_ON =request.find('/?LED2=ON')
  LED2_OFF =request.find('/?LED2=OFF')
  
  LED3_ON =request.find('/?LED3=ON')
  LED3_OFF =request.find('/?LED3=OFF')
  
  LED4_ON =request.find('/?LED4=ON')
  LED4_OFF =request.find('/?LED4=OFF')
  
  #fans
  FAN1_ON =request.find('/?FAN1=ON')
  FAN1_OFF =request.find('/?FAN1=OFF')
  
  FAN2_ON =request.find('/?FAN2=ON')
  FAN2_OFF =request.find('/?FAN2=OFF')
  
  FAN3_ON =request.find('/?FAN3=ON')
  FAN3_OFF =request.find('/?FAN3=OFF')
  
  if(LED1_ON==6):
    LED1.value(1)   
  if(LED1_OFF==6):
    LED1.value(0)
    
  if(LED2_ON==6):
    LED2.value(1)   
  if(LED2_OFF==6):
    LED2.value(0)
    
  if(LED3_ON==6):
    LED3.value(1)   
  if(LED3_OFF==6):
    LED3.value(0)
    
  if(LED4_ON==6):
    LED4.value(1)   
  if(LED4_OFF==6):
    LED4.value(0)
    
  #Fans
  if(FAN1_ON==6):
    FAN1.value(1)   
  if(FAN1_OFF==6):
    FAN1.value(0)
    
  if(FAN2_ON==6):
    FAN2.on()   
  if(FAN2_OFF==6):
    FAN2.off()
    
  if(FAN3_ON==6):
    FAN3.value(1)   
  if(FAN3_OFF==6):
    FAN3.value(0)
    
  # Sending HTML document in response everytime to all connected clients  
  response=html 
  connection_socket.send(response)
  
  #Closing the socket
  connection_socket.close()

