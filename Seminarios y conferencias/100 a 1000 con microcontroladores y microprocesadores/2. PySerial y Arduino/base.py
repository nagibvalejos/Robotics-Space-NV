import mysql.connector as mc
import time
class Base:

    def __init__(self):
        self.cnx = mc.connect(user='root',password="contraseña",database='temperatura')
        self.cursor = self.cnx.cursor()

    def insertar_dato(self,value):
        instruccion = ("INSERT INTO medida(temperatura,fecha,hora) VALUES(%s,%s,%s)")

        hora = time.strftime('%H:%M:%S')
        fecha = time.strftime("%d/%m/%y")

        dato = (value,fecha,hora)

        self.cursor.execute(instruccion,dato)
        self.cnx.commit()


    def cerrar_base(self):
        self.cursor.close()
        self.cnx.close()

