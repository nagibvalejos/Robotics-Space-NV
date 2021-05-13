from machine import Pin
import utime
pir = Pin(28,Pin.IN,Pin.PULL_DOWN)
rojo = Pin(16,Pin.OUT)
def pir_handler(pin):
    utime.sleep_ms(100)
    if pin.value():
        print("Alarma! Movimiento detectado!")
        for i in range(50):
            rojo.toggle()
            utime.sleep_ms(100)
pir.irq(trigger=Pin.IRQ_RISING,handler=pir_handler)