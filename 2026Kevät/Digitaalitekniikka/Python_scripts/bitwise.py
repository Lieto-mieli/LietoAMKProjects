from machine import ADC, Pin
import time
button = Pin(12, Pin.IN, Pin.PULL_UP)
led0 = Pin(20, Pin.OUT)
led1 = Pin(21, Pin.OUT)
led2 = Pin(22, Pin.OUT)
leds = [led2, led1, led0]
num = 0
while True:
    if button.value() == 0:
        time.sleep(0.150)
        if button.value() == 0:
            if num==7:
                num=0
            else:
                num = num+1
            print(num)
            n = num
            bit = 0
            while n > 0:
                curLed = leds[bit]
                res = n & 1
                if res == 1:
                    curLed.on()
                else:
                    curLed.off()
                n >>= 1
                bit = bit+1
            while bit < 3:
                leds[bit].off()
                bit = bit+1