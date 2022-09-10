import camera

uart1 = UART(1, baudrate=9600, tx=33, rx=32)
camera.init()
img = camera.capture()
imgFile = open("photo.jpg", "wb")
imgFile.write(img)
imgFile.close()
import os
os.listdir()