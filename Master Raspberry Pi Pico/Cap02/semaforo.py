from machine import Pin
import utime
rojo = Pin(15,Pin.OUT)
amarillo = Pin (13,Pin.OUT)
verde = Pin(16,Pin.OUT)

while True:
    rojo.value(0)
    verde.value(1) #encendiendo el led verde
    utime.sleep_ms(2000)
    verde.value(0)
    amarillo.value(1) 
    utime.sleep_ms(1000)
    amarillo.value(0)
    rojo.value(1) 
    utime.sleep_ms(2000)
    