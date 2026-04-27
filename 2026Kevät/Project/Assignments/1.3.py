import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

down_button = Pin(9, Pin.IN, Pin.PULL_UP)
reset_button = Pin(8, Pin.IN, Pin.PULL_UP)
up_button = Pin(7, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

oled.fill(0)
x=0
y=31
while True:
    oled.pixel(x,y,1)
    if down_button() == 0:
        if y<63:
            y+=1
    if up_button() == 0:
        if y>0:
            y-=1
    if reset_button() == 0:
        oled.fill(0)
        x=0
        y=31
    oled.show()
    if x<127:
        x+=1
    else:
        x=0