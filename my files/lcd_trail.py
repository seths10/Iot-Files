from ST7735 import Display
import fonts.sysfont as sysfont
from machine import SPI,Pin
import time
import math
import sys

if sys.platform == 'esp32':
    sck = Pin(18)
    miso= Pin(19)
    mosi= Pin(23)
    SPI_CS = 26
    SPI_DC = 5
    spi = SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)
    
tft=Display(spi,SPI_CS,SPI_DC)

tft.clear()
tft.draw_hline(0,35 , tft.size()[0], Display.WHITE)
tft.draw_text(0, 40, "Temperature: ", sysfont, Display.WHITE)
# tft.draw_text(75, 40, str(temp), sysfont, Display.YELLOW)
tft.draw_text(0, 60, "Humidity: ", sysfont, Display.WHITE)
# tft.draw_text(75, 60, str(hum), sysfont, Display.YELLOW)
tft.draw_hline(0,70 , tft.size()[0], Display.WHITE)
time.sleep(10)
