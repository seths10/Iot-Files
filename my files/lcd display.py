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
    tft=Display(spi,SPI_DC,SPI_CS)
    
tft=Display(spi,SPI_CS,SPI_DC)
        
        
def main():
    tft.clear()
    tft.draw_text(0, 0, "Loading...", sysfont, Display.YELLOW)

    
    tft.draw_text(0, 0, "Loading...", sysfont, Display.RED)

    
    tft.draw_text(0, 0, "Loading...", sysfont, Display.ORANGE)

    
    tft.draw_text(0, 0, "Loading...", sysfont, Display.BLUE)


    tft.draw_text(0, 0, "Loading...", sysfont, Display.PINK)

               
    tft.draw_text(0, 0, "Loading...", sysfont, Display.YELLOW)

    
    tft.draw_text(0, 0, "Loading...", sysfont, Display.RED)

    
    tft.draw_text(0, 0, "Loading...", sysfont, Display.ORANGE)

    
    tft.draw_text(0, 0, "Loading...", sysfont, Display.BLUE)
  

    tft.draw_text(0, 0, "Loading...", sysfont, Display.PINK)


    tft.draw_text(0, 0, "Loading...", sysfont, Display.YELLOW)

    
    tft.draw_text(0, 0, "Loading...", sysfont, Display.RED)

    
    tft.draw_text(0, 0, "Loading...", sysfont, Display.ORANGE)

    
    tft.draw_text(0, 0, "Loading...", sysfont, Display.BLUE)


    tft.draw_text(0, 0, "Loading...", sysfont, Display.PINK)


    tft.draw_text(0, 0, "Loading...", sysfont, Display.YELLOW)

    
    tft.draw_text(0, 0, "Loading...", sysfont, Display.RED)
    
    tft.draw_text(0, 0, "Loading...", sysfont, Display.ORANGE)

    
    tft.draw_text(0, 0, "Loading...", sysfont, Display.BLUE)


    tft.draw_text(0, 0, "Loading...", sysfont, Display.WHITE)
    
    tft.draw_hline(0,12 , tft.size()[0], Display.WHITE)
    tft.clear()
    
    tft.draw_text(35,60, "I am Seth!", sysfont, Display.YELLOW)
    


main()
