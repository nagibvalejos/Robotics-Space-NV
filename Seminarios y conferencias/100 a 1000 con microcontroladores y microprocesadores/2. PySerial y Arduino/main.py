import interfaz
import tkinter
import user_serial
import threading
import time
import serial
import base

def actualizardatos():
    tiempo = 0
    while ciclo:
        value = s.read_serial()
        if value != "":
            try:
                frame_widgets.actualizar_txt(value)
                frame_interfaz.cambiar_valor(value)
                frame_grafica.dibujar_punto(float(value),tiempo)
                conexion.insertar_dato(value)
                tiempo+=1
            except:
                pass
    print("Terminé el hilo")

def close():#cerrar todo tipo de conexion
    root.destroy()
    global ciclo
    ciclo = False#cambiamos el valor para que ya no se vuelva a ejecutar el ciclo while otra vez
    t.join()#esperar al que el hilo termine su última tarea
    s.close()
    conexion.cerrar_base()
    

#conexion a la base de datos
conexion = base.Base()

#perteneciente al hilo
ciclo = True#controla el while de la función perteneciente al hilo
s = user_serial.User_Serial('COM1',9600)
t = threading.Thread(target=actualizardatos)
t.start()
#perteneciente al hilo

root = tkinter.Tk()
ancho,alto = 820,500
root.geometry(f'{ancho}x{alto}')
root.resizable(False,False)
root.title("Adquisición de Datos")

frame_interfaz = interfaz.Interfaz(root,ancho,alto)
frame_widgets = interfaz.Mostrar_Dato(root,ancho,alto)
frame_grafica = interfaz.Grafica(root,ancho,alto)

frame_interfaz.grid(row=0,column=0,rowspan=2,sticky="ns")
frame_widgets.grid(row=0,column=1,sticky="nsew")
frame_grafica.grid(row=1,column=1,sticky="nsew")

root.rowconfigure(1,weight=1)
root.columnconfigure(1,weight=1)

root.protocol('WM_DELETE_WINDOW',close)
root.mainloop()