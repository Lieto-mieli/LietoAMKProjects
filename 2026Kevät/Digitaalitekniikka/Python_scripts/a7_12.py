from machine import ADC, Pin
import time
button = Pin(7, Pin.IN, Pin.PULL_UP)
alarm = Pin(9, Pin.IN, Pin.PULL_UP)
red_lamp = Pin(22, Pin.OUT)
siren = Pin(20, Pin.OUT)
state = "OFF"
red_lamp.off()
siren.off()
while True:
    time.sleep(0.200)#5 Hz. The ASM-chart template says to go with 10 μs but that is too fast to really see the blinking
    if state == "OFF":
        if alarm.value() == 0:
            state = "A"
            red_lamp.on()
            siren.on()
    elif state == "A":
        if alarm.value() == 1:
            state = "AB"
            red_lamp.on()
            siren.off()
        elif button.value() == 0:
            state = "B1"
            red_lamp.on()
            siren.off()
    elif state == "AB":
        if button.value() == 0:
            state = "OFF"
            red_lamp.off()
            siren.off()
    elif state == "B1":
        if alarm.value() == 0:
            state = "B2"
            red_lamp.off()
        elif alarm.value() == 1:
            state = "OFF"
            red_lamp.off()
    elif state == "B2":
        if alarm.value() == 0:
            state = "B1"
            red_lamp.on()
        elif alarm.value() == 1:
            state = "OFF"
    print(state)