import serial
import time

class User_Serial:

    def __init__(self,port,baudrate):

        self.s = serial.Serial(port=port,baudrate=baudrate)
        time.sleep(2)
        self.s.reset_input_buffer()

    def read_serial(self):
        data = ""
        if self.s.inWaiting()>0:
            data = self.s.read_until(b'\n')
            data = data.decode()
        return data

    def clear_buffer_input(self):
        self.s.reset_input_buffer()

    def write_serial(self,message):
        message +='\n'
        data = self.s.write(message.encode())

    def close(self):
        self.s.close()