from machine import Pin
import utime
pir = Pin(28,Pin.IN,Pin.PULL_DOWN)

def pir_handler(pin):
    utime.sleep_ms(100)
    if pin.value():
        print("Alarma! Movimiento detectado!")
        
pir.irq(trigger=Pin.IRQ_RISING,handler=pir_handler)