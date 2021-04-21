from machine import Pin
import utime
amarillo = Pin(17,Pin.OUT)
azul = Pin(19,Pin.OUT)
pulsador2 = Pin(14,Pin.IN,Pin.PULL_UP)

while True:
    if pulsador2.value() == 0:
        amarillo.on()
        azul.off()
        utime.sleep(1)
        amarillo.off()
        azul.on()
        utime.sleep(1)
    else:
        azul.off()