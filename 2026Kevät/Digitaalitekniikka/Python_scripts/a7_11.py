from machine import ADC, Pin
import time
button = Pin(7, Pin.IN, Pin.PULL_UP)
led = Pin(20, Pin.OUT)
state = "OFF"
led.off()
while True:
    time.sleep(0.050)
    if state == "OFF":
        if button.value() == 0:
            state = "ONW"
            led.on()
    elif state == "ONW":
        if button.value() == 1:
            state = "ON"
            led.on()
    elif state == "ON":
        if button.value() == 0:
            state = "OFFW"
            led.off()
    elif state == "OFFW":
        if button.value() == 1:
            state = "OFF"
            led.off()
    print(state)