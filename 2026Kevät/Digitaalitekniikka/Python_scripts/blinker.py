from machine import ADC, Pin
import time
adc = ADC(Pin(26))
led = Pin("LED", Pin.OUT)
led_state = 1
while True:
    val = adc.read_u16()
    time.sleep(val/65535)
    print(val)
    if(led_state == 1):
        led.off()
        led_state = 0
    elif(led_state == 0):
        led.on()
        led_state = 1