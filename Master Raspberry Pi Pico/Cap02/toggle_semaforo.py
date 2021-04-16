from machine import Pin
import utime
rojo = Pin(15,Pin.OUT)
amarillo = Pin (13,Pin.OUT)
verde = Pin(16,Pin.OUT)

while True:
    verde.toggle() #encendiendo el led verde
    utime.sleep_ms(2000)
    amarillo.toggle() 
    utime.sleep_ms(1000)
    rojo.toggle() 
    utime.sleep_ms(2000)