import tkinter
import tkinter.ttk
class Interfaz(tkinter.LabelFrame):#termometro

    def __init__(self,master,ancho,alto):
        super().__init__(master)

        self.c = tkinter.Canvas(self,bg="white")

        self.c.create_rectangle(140,10,190,alto-10)#contorno
        self.alto = alto
        self.temperatura = self.c.create_rectangle(141,alto-10,189,alto-10,fill = "red")#contorno

        #construyendo la regla
        self.tempmax = 20
        self.tempmin = 0
        val = self.tempmax
        for i in range(10,alto-10+1):
            medida = self.map(val,self.tempmax,self.tempmin,10,alto-10+1)
            self.c.create_text(130,medida,text=str(val))
            val-=1
        #construyendo la regla

        self.c.pack(expand=True,fill="both")

    def map(self,x,in_min,in_max,out_min,out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def cambiar_valor(self,valor):
        valor = float(valor)
        valor = self.map(valor,self.tempmin,self.tempmax,self.alto-10+1,10)

        self.c.delete(self.temperatura)
        self.temperatura = self.c.create_rectangle(141,valor,189,self.alto-10,fill = "red")

class Mostrar_Dato(tkinter.LabelFrame):#en una caja de texto los datos
    def __init__(self,master,ancho,alto):
        super().__init__(master)

        lbltitulo = tkinter.Label(self,text="Adquisicion de Temperatura")
        lbltemp = tkinter.Label(self,text="Temperatura Leida:")
        self.txttemp = tkinter.ttk.Entry(self)

        lbltitulo.grid(row=0,column=0,columnspan=2)
        lbltemp.grid(row=1,column=0)
        self.txttemp.grid(row=1,column=1)

        self.columnconfigure(0,weight=1)
        
    
    def actualizar_txt(self,value):
        self.txttemp.delete(0,'end')
        self.txttemp.insert(0,str(value))
        
class Grafica(tkinter.LabelFrame):#grafica en tiempo real
    def __init__(self,master,ancho,alto):
        super().__init__(master)

        self.canvas = tkinter.Canvas(self,bg="white")

        #centtro 0,0 = 30,430
        #coordenada vertical = 30,35
        #coordenada horizontal = 385,430

        self.canvas.create_line(30,30,30,430)
        self.canvas.create_polygon(20,30,40,30,30,20)
        self.canvas.create_text(20,10,text="T(°C)")
        for i in range(21):
            value = self.map(i,0,20,430,35)
            self.canvas.create_text(20,value,text=str(i))

        self.canvas.create_line(30,430,395,430)
        self.canvas.create_polygon(395,420,395,440,400,430)
        self.canvas.create_text(410,430,text="t(s)")
        self.maxtiempo = 10
        self.mintiempo = 0
        self.etiquetas_tiempo = []
        for i in range(11):
            value = self.map(i,self.mintiempo,self.maxtiempo,30,385)
            e = self.canvas.create_text(value,440,text=str(i))
            self.etiquetas_tiempo.append(e)

        self.canvas.pack(expand=True,fill="both")
        self.coordenadas=[]
        self.lineas = []
        self.puntos = []

    def map(self,x,in_min,in_max,out_min,out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def dibujar_punto(self,medida,tiempo):


        if tiempo == self.maxtiempo+1:
            self.mintiempo = self.maxtiempo
            self.maxtiempo += 10
            for i in self.lineas:
                self.canvas.delete(i)
            self.lineas=[]
            for i in self.puntos:
                self.canvas.delete(i)
            newvalue = self.mintiempo
            for i in self.etiquetas_tiempo:
                self.canvas.itemconfig(i,text=str(newvalue))
                newvalue+=1
            self.puntos=[]
            ultimacoord = self.coordenadas[-1]
            oval = self.canvas.create_oval(30,ultimacoord[1],30,ultimacoord[1],width=2.0)
            self.puntos.append(oval)
            self.coordenadas=[[30,ultimacoord[1]]]#añadir los pares de coordenadas

        value_medida = self.map(medida,0,20,430,35)
        value_tiempo = self.map(tiempo,self.mintiempo,self.maxtiempo,30,385)
        
        oval = self.canvas.create_oval(value_tiempo,value_medida,value_tiempo,value_medida,width=2.0)
        self.puntos.append(oval)

        #dibujar linea entre puntos
        if len(self.coordenadas) !=0:
            par_coord = self.coordenadas[-1]
            linea = self.canvas.create_line(par_coord[0],par_coord[1],value_tiempo,value_medida)
            self.lineas.append(linea)

        self.coordenadas.append([value_tiempo,value_medida])#añadir los pares de coordenadas