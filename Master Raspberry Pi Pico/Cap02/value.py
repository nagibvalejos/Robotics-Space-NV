from machine import Pin
import utime
amarillo = Pin (13,Pin.OUT)

while True:
    amarillo.value(1) #amarillo.on()
    utime.sleep_ms(1000)
    amarillo.value(0) #amarillo.off()
    utime.sleep_ms(1000)