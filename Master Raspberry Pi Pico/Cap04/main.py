from machine import Pin
import utime

R = Pin(16,Pin.OUT)
G = Pin(17,Pin.OUT)
rojo = Pin(18,Pin.OUT)
amarillo = Pin(19,Pin.OUT)
verde = Pin(20,Pin.OUT)
buzzer = Pin(21,Pin.OUT)
while True:
    rojo.off()
    verde.on()
    R.on()
    G.off()
    for i in range (3):
        buzzer.on()
        utime.sleep_ms(500)
        buzzer.off()
        utime.sleep_ms(500)
    verde.off()
    amarillo.on()
    for i in range (5):
        buzzer.on()
        utime.sleep_ms(100)
        buzzer.off()
        utime.sleep_ms(100)
    amarillo.off()
    rojo.on()
    R.off()
    G.on()
    utime.sleep(3)