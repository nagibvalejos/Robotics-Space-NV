from machine import Pin
import utime
foquito = Pin(25,Pin.OUT)

while True:
    foquito.on()
    utime.sleep_ms(1000)
    foquito.off()
    utime.sleep_ms(1000)