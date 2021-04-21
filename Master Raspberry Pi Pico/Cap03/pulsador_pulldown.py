from machine import Pin
import utime
amarillo = Pin(17,Pin.OUT)
pulsador = Pin(15,Pin.IN,Pin.PULL_DOWN)

while True:
    if pulsador.value() == 1:
        amarillo.on()
    else:
        amarillo.off()