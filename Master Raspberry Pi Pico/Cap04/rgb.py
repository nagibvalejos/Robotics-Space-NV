from machine import Pin
import utime

rojo = Pin(16,Pin.OUT)
verde = Pin(17,Pin.OUT)
azul = Pin(18,Pin.OUT)
while True:
    azul.off()
    rojo.on()
    utime.sleep_ms(500)
    rojo.off()
    verde.on()
    utime.sleep_ms(500)
    verde.off()
    azul.on()
    utime.sleep_ms(500)