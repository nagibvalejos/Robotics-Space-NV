from machine import Pin
import utime
amarillo = Pin (13,Pin.OUT)

while True:
    amarillo.toggle() #palanca
    utime.sleep_ms(1000)