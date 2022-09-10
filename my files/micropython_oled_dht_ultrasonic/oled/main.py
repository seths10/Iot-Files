from machine import Pin, I2C
import ssd1306
from time import sleep

i2c =I2C(-1,scl=Pin(22), sda=Pin(21))

oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3c)
oled.fill(0)
oled.text("Hello World",30,30)
oled.show()

sleep(10)
oled.fill(0)
oled.show()

oled. line ( 10,10,80,20,1) # Draw an illuminated line. Origin (4, 5) and final (80,20)      
oled. show ( ) # Show result

sleep(5)
oled.fill(0)
oled.show()

oled. hline ( 5,30,100,1 ) # Draw an illuminated horizontal line. Origin (5, 30) width 100 pixels      
oled. show () # Show result

sleep(5)
oled.fill(0)
oled.show()

oled. vline (50,5,60,1) # Draw an illuminated vertical line. Origin (50, 5) height 60 pixels     
oled. show () # Show result

sleep(5)
oled.fill(0)
oled.show()

oled.rect (15,10,60,40,1 ) # Draw an illuminated rectangle. Origin (15,10) and width x height 60x40 pixels     
oled.show () # Show result

sleep(5)
oled.fill(0)
oled.show()

oled.fill_rect ( 20,10,60,40,1 ) # Draw an illuminated filled rectangle. Origin (20,10) and width x height 60x40 pixels     
oled.show () # Show result

sleep(5)
oled.fill(0)
oled.show()

oled.text("ALSELECTRO.COM",0,30)
oled.show()