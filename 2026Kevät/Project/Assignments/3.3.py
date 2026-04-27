#assignment 3.3
import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C
from filefifo import Filefifo


start_button = Pin(8, Pin.IN, Pin.PULL_UP)
rotA = Pin(10, Pin.IN, Pin.PULL_UP)
rotB = Pin(11, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)

oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

oled.fill(0)
run=False
oled.text("Task 3.3",32,26,1)
oled.text("press SW1",32,39,1)
oled.show()

curMax = 0
curMin = 65535


place = 0

def turnA_handler(pin):
    if rotB.value():
        Turn("B")
    else:
        Turn("A")

rotA.irq(handler = turnA_handler, trigger = Pin.IRQ_FALLING)

values = []
def Turn(dir):
    global place
    oled.fill(0)
    if dir=="B":
        if place<2530-256:
            place +=2
            oled.scroll(-2,0)
    if dir=="A":
        if place>0:
            place -=2
            oled.scroll(2,0)
            #print(values[place]-curMin/curMax-curMin)
            #print(int(63*(values[place]-curMin/curMax-curMin)))
    for i in range(255):
        oled.pixel(int(i/2),int(63*((values[place+i]-curMin)/(curMax-curMin))),1)
    oled.show()
while True:
    if run:

        
        run=False
    else:
        if start_button() == 0:
            fifo = Filefifo(10,name = 'week3_data.txt')
            for _ in range(1000):
                if fifo.has_data():
                    data = fifo.get()
                    values.append(data)
                    if data<curMin:
                        curMin=data
                    if data>curMax:
                        curMax=data
            for _ in range(1530):
                if fifo.has_data():
                    data = fifo.get()
                    values.append(data)
            run=True
            oled.fill(0)
            oled.show()