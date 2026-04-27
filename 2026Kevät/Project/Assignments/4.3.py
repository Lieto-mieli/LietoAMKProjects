#assignment 4.3
import time, micropython
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C
from fifo import Fifo
from piotimer import Piotimer

samples = Fifo(50)
micropython.alloc_emergency_exception_buf(100)

start_button = Pin(8, Pin.IN, Pin.PULL_UP)
rotA = Pin(10, Pin.IN, Pin.PULL_UP)
rotB = Pin(11, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
led = Pin(22, Pin.OUT)
crowtail = machine.ADC(26)

oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

oled.fill(0)
run=False
oled.text("Task 4.3",32,26,1)
oled.text("press SW1",32,39,1)
oled.show()

led.off()

curMax = 0
curMin = 65535
threshold = 32767
thresholdp = 0.50


place = 0

def turnA_handler(pin):
    if rotB.value():
        Turn("B")
    else:
        Turn("A")

rotA.irq(handler = turnA_handler, trigger = Pin.IRQ_FALLING)

values = []
def Turn(dir):
    global thresholdp
    if dir=="B":
        if thresholdp<1:
            thresholdp +=0.01
    if dir=="A":
        if thresholdp>0:
            thresholdp -=0.01

def Feed(tid):
    #print(crowtail.read_u16())
    samples.put(crowtail.read_u16())
while True:
    if run:
        if samples.has_data():
            values.append(samples.get())
            if values[len(values)-1]>threshold:
                led.on()
            else:
                led.off()
        if len(values)>500:
            curMax = 0
            curMin = 65535
            for i in range(len(values)):
                #print(len(values))
                #print(i)
                if values[i]<curMin:
                    curMin=values[i]
                if values[i]>curMax:
                    curMax=values[i]
            values = []
            threshold = curMin+((curMax-curMin)*thresholdp)
            oled.fill(0)
            print(threshold)
            oled.text("Threshold: "+str(threshold),0,0,1)
            print(thresholdp)
            oled.text("T. Percent: "+str(int(thresholdp*100))+"%",0,10,1)
            print(curMin)
            oled.text("Minimum: "+str(curMin),0,20,1)
            print(curMax)
            oled.text("Maximum: "+str(curMax),0,30,1)
            oled.show()
    else:
        if start_button() == 0:
            tmr = Piotimer(period=4, mode=Piotimer.PERIODIC, callback=Feed)
            run=True
            oled.fill(0)
            oled.show()