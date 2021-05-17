from machine import Pin, UART
from utime import sleep
in1 = Pin(17,Pin.OUT)
in2 = Pin(16,Pin.OUT)
in3 = Pin(15,Pin.OUT)
in4 = Pin(14,Pin.OUT)
#bt = UART(puerto,velocidad)
bt = UART(0,9600)

while True:
    dato = bt.read(1) #if(Serial.available()>0) dato=Serial.read()
    if "A" in dato:
        in1.on()
        in2.off()
        in3.on()
        in4.off()
    if "R" in dato:
        in1.value(0)
        in2.value(1)
        in3.value(0)
        in4.value(1)
    if "I" in dato:
        in1.value(0)
        in2.value(1)
        in3.value(1)
        in4.value(0)
    if "D" in dato:
        in1.on()
        in2.off()
        in3.off()
        in4.on()
    if "P" in dato:
        in1.off()
        in2.off()
        in3.off()
        in4.off()