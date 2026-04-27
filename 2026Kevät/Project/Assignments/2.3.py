#assignment 2.3
import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C
from filefifo import Filefifo


start_button = Pin(8, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)

oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

oled.fill(0)
run=False
oled.text("Task 2.3",32,26,1)
oled.text("press SW1",32,39,1)
oled.show()

curMax = 0
curMin = 65535
curAvg = 0

while True:
    if run:
        fifo = Filefifo(10,name = 'sinewave_250Hz_03.txt')
        for _ in range(500):
            if fifo.has_data():
                data = fifo.get()
                if data<curMin:
                    curMin=data
                if data>curMax:
                    curMax=data
                #print(data)
        curAvg=(curMax+curMin)/2
        print(curAvg)
        
        peak=False
        counting=False
        samplesSincePeak=0
        intList = []
        
        for _ in range(1000):
            if fifo.has_data():
                data = fifo.get()
                if counting:
                    samplesSincePeak+=1
                if peak==False:
                    if data>curAvg:
                        peak=True
                        if counting:
                            intList.append(samplesSincePeak)
                            print(samplesSincePeak)
                            samplesSincePeak=0
                        counting=True
                if peak==True:
                    if data<curAvg:
                        peak=False
                #print(data)
        c=0
        freq=0
        for i in range(4):
            oled.text(str(i+1)+")int:"+str(intList[i])+"-"+str(intList[i]*4)+"ms",0,c*12,1)
            c+=1
            freq+=intList[i]
        freq = freq/1000
        oled.text("freq "+str(round(1/freq,5))+"hz",0,4*12,1)
        oled.show()
        run=False
    else:
        if start_button() == 0:
            run=True
            oled.fill(0)
            oled.show()
