import tkinter as tk

from tkinter import filedialog
from PIL import ImageTk, Image
import Ruido
import Operaciones
import Histograma
import Filtros
import Mofos
import sys

from Umbral import *
from time import sleep

rec = "recovery.jpg"
act = "inuse.jpg"
def Cerrar():
    pass
def abrir():
   pic = filedialog.askopenfilename()
   aux1 = Image.open(pic)
   aux1.save(act)

   o_size = aux1.size   #Tamaño original de la imagen
   f_size = (aux1.size) #Tamaño del canvas donde se mostrará la imagen

   imgr = ImageTk.PhotoImage(aux1)
  
   canvas = tk.Canvas(root, width=f_size[0], height= f_size[1])
   canvas.delete("all")
   canvas.create_image(f_size[0]/2, f_size[1]/2, anchor=tk.CENTER, image=imgr, tags="img")
   canvas.grid(row=0, column=0, columnspan=5, rowspan=3)
   root.mainloop()

def restaurar ():

   aux1 = Image.open(rec)
   aux1.save(act)
   sleep(.5)
   #aux1.show()
   o_size = aux1.size   #Tamaño original de la imagen
   f_size = (aux1.size) #Tamaño del canvas donde se mostrará la imagen

   imgr = ImageTk.PhotoImage(aux1)
   
   canvas = tk.Canvas(root, width=f_size[0], height= f_size[1])
   canvas.create_image(f_size[0]/2, f_size[1]/2, anchor=tk.CENTER, image=imgr, tags="img")
   canvas.grid(row=0, column=0, columnspan=5, rowspan=3)
   root.mainloop()

   aux1.close()
def funcion(*argv):
   #print ("Valor "+argv[1])
   #Ruido.additivo(img,.1)
   auxF = Image.open(act)
   auxF.save(rec)
   
   if (argv[0]==1):
      imgF = Ruido.aditivo(auxF,float(argv[1]))
   elif (argv[0]==2):
      imgF = Ruido.sustractivo(auxF,float(argv[1]))
   elif (argv[0]==3):
      imgF = Ruido.pimienta(auxF,float(argv[1]))
   elif (argv[0]==4):
      op = Umbral()
      op.addHistorial(auxF)
      imgF = op.umbral(int(argv[1]) ,auxF)
   elif(argv[0]==5) :
      op = Umbral()
      op.addHistorial(auxF)
      imgF = op.escala(auxF)
   elif(argv[0]==6) :
      op = Umbral()
      op.addHistorial(auxF)
      imgF = op.rgb(auxF,argv[1] )
   elif (argv[0]==12):
      imgF = Image.open(act)
      Histograma.histogramaRGB(auxF)
   elif ( argv[0] == 13 ):
      imgF = Histograma.desplazamiento(auxF, int(argv[1]) )
      Histograma.histogramaG(imgF)  
   elif ( argv[0] == 14 ):
      imgF = Histograma.contraccion(auxF, int(argv[1]),int (argv[2]))
      Histograma.histogramaG(imgF)
   elif (argv[0] == 15):
      imgF = Histograma.expansion(auxF, 0 , 255 )
      Histograma.histogramaG(imgF)
   elif (argv[0]==16):
      imgF = Filtros.pasa_bajas_prom(auxF)
   elif (argv[0]==17):
      imgF =  Filtros.pasa_bajas_moda(auxF)
   elif (argv[0]==18):
      imgF =  Filtros.pasa_bajas_media(auxF)
   elif (argv[0]==19):
      imgF =  Mofos.dilatacion(auxF)
   elif (argv[0]==20):
      op = Umbral()
      op.addHistorial(auxF)
      imgF2 = op.umbral(150 ,auxF)
      imgF =  Mofos.erosion(imgF2)
   elif (argv[0]==21):
      op = Umbral()
      op.addHistorial(auxF)
      imgF2 = op.umbral(150 ,auxF)
      imgF =  Mofos.contorno(imgF2)
   elif (argv[0]==22):
      op = Umbral()
      op.addHistorial(auxF)
      imgF2 = op.umbral(150 ,auxF)
      imgF =  Mofos.apertura(imgF2)
   elif (argv[0]==23):
      op = Umbral()
      op.addHistorial(auxF)
      imgF2 = op.umbral(150 ,auxF)
      imgF =  Mofos.cierre(imgF2)
   

   auxF.close()
   imgF.save(act)
   o_size = imgF.size   #Tamaño original de la imagen
   f_size = (imgF.size) #Tamaño del canvas donde se mostrará la imagen
   img2 = ImageTk.PhotoImage(imgF)
   
   canvas = tk.Canvas(root, width=f_size[0], height= f_size[1])
   canvas.create_image(f_size[0]/2, f_size[1]/2, anchor=tk.CENTER, image=img2, tags="img")
   canvas.grid(row=0, column=0, columnspan=5, rowspan=3)
   auxF.close()
   root.mainloop()
  # print("First Name: %s\nLast Name: %s" % (entry1.get(), entry1.get()))
def win2():
    tl = tk.Toplevel(root)
    tl.title("Modificar Datos")
    tl.geometry('100x300')
    tl.focus_set()
    tl.grab_set()
    tl.transient(master=root)

    inf = tk.StringVar(tl)
    entry1 = tk.Entry(tl, textvariable=inf)
    entry1.grid(row=0, column=1)
    label1 = tk.Label(tl, text='Porcentaje (0,1)')
    label1.grid(row=0, column=0)
    b = tk.Button(tl,text="generar", command=funcion('h'))
    t1.wait_window(t1)

    b.pack()
def ruidoA():
    tl = tk.Toplevel(root)
    tl.title("Ruido aditivo")
    tl.geometry('300x100')
    tl.focus_set()
    tl.grab_set()
    tl.transient(master=root)

    inf = tk.StringVar(tl)
    entry1 = tk.Entry(tl, textvariable=inf)
    entry1.grid(row=0, column=1)
    label1 = tk.Label(tl, text='Porcentaje (0,1)')
    label1.grid(row=0, column=0)
    b = tk.Button(tl,text="Generar", command=lambda:funcion(1,entry1.get() )).grid(row=1, column=0)
def ruidoS():
    tl = tk.Toplevel(root)
    tl.title("Ruido sustractivo")
    tl.geometry('300x100')
    tl.focus_set()
    tl.grab_set()
    tl.transient(master=root)

    inf = tk.StringVar(tl)
    entry1 = tk.Entry(tl, textvariable=inf)
    entry1.grid(row=0, column=1)
    label1 = tk.Label(tl, text='Porcentaje (0,1)')
    label1.grid(row=0, column=0)
    b = tk.Button(tl,text="Generar", command=lambda:funcion(2,entry1.get())).grid(row=1, column=0)
def canales():
    tl = tk.Toplevel(root)
    tl.title("Canales RGB")
    tl.geometry('300x100')
    tl.focus_set()
    tl.grab_set()
    tl.transient(master=root)

    inf = tk.StringVar(tl)
    entry1 = tk.Entry(tl, textvariable=inf)
    entry1.grid(row=0, column=1)
    label1 = tk.Label(tl, text='Canal r, g, b')
    label1.grid(row=0, column=0)
    b = tk.Button(tl,text="Generar", command=lambda:funcion(6,entry1.get())).grid(row=1, column=0)
def ruidoP():
    tl = tk.Toplevel(root)
    tl.title("Ruido aditivo")
    tl.geometry('300x100')
    tl.focus_set()
    tl.grab_set()
    tl.transient(master=root)

    inf = tk.StringVar(tl)
    entry1 = tk.Entry(tl, textvariable=inf)
    entry1.grid(row=0, column=1)
    label1 = tk.Label(tl, text='Porcentaje (0,1)')
    label1.grid(row=0, column=0)
    b = tk.Button(tl,text="Generar", command=lambda:funcion(3,entry1.get())).grid(row=1, column=0)
def contraccionH():
    tl = tk.Toplevel(root)
    tl.title("Contraccion del histograma")
    tl.geometry('300x100')
    tl.focus_set()
    tl.grab_set()
    tl.transient(master=root)

    inf = tk.StringVar(tl)
    entry1 = tk.Entry(tl, textvariable=inf)
    entry1.grid(row=0, column=1)
    label1 = tk.Label(tl, text='CMIN  ')
    label1.grid(row=0, column=0)
   
    inf2 = tk.StringVar(tl)
    entry2 = tk.Entry(tl, textvariable=inf2)
    entry2.grid(row=1, column=1)
    label1 = tk.Label(tl, text='CMAX  ')
    label1.grid(row=1, column=0)
    b = tk.Button(tl,text="Generar", command=lambda:funcion( 14 ,entry1.get(), entry2.get() ) ).grid(row=2, column=0)

def deslpazamientoH():
    tl = tk.Toplevel(root)
    tl.title("Desplazamiento del histograma")
    tl.geometry('300x100')
    tl.focus_set()
    tl.grab_set()
    tl.transient(master=root)

    inf = tk.StringVar(tl)
    entry1 = tk.Entry(tl, textvariable=inf)
    entry1.grid(row=0, column=1)
    label1 = tk.Label(tl, text='Despazamiento (-255,255)')
    label1.grid(row=0, column=0)
    b = tk.Button(tl,text="Generar", command=lambda:funcion( 13 ,entry1.get())).grid(row=1, column=0)

def umbral():
    tl = tk.Toplevel(root)
    tl.title("Umbral")
    tl.geometry('300x100')
    tl.focus_set()
    tl.grab_set()
    tl.transient(master=root)

    inf = tk.StringVar(tl)
    entry1 = tk.Entry(tl, textvariable=inf)
    entry1.grid(row=0, column=1)
    label1 = tk.Label(tl, text='Umbral (0,255)')
    label1.grid(row=0, column=0)
    b = tk.Button(tl,text="Generar", command=lambda:funcion(4,entry1.get())).grid(row=1, column=0)

root = tk.Tk()
#pic = sys.argv[1]
#pic = "snakes.jpg"
pic = filedialog.askopenfilename()

img = Image.open(pic)
img.save(act)

o_size = img.size   #Tamaño original de la imagen
f_size = (img.size) #Tamaño del canvas donde se mostrará la imagen

img2 = ImageTk.PhotoImage(img)
img.close()

canvas = tk.Canvas(root, width=f_size[0], height= f_size[1])
canvas.create_image(f_size[0]/2, f_size[1]/2, anchor=tk.CENTER, image=img2, tags="img")
canvas.grid(row=0, column=0, columnspan=5, rowspan=3)

boton = tk.Button(root, text="Ruido Aditivo", command=ruidoA).grid(row=3, column=0)
boton = tk.Button(root, text="Ruido Sustractivo", command=ruidoS).grid(row=3, column=1)
botoImageTkn = tk.Button(root, text="Ruido Sal y pimienta", command=ruidoP).grid(row=3, column=2)

boton = tk.Button(root, text="Umbralizacion", command=umbral).grid(row=4, column=0)
boton = tk.Button(root, text="Escala de grices", command=lambda:funcion(5,"5")).grid(row=4, column=1)
boton = tk.Button(root, text="canales RGB", command=canales).grid(row=4, column=2)

boton = tk.Button(root, text="Operacion Suma ", command=funcion).grid(row=5, column=0)
boton = tk.Button(root, text="Operacion Resta ", command=funcion).grid(row=5, column=1)

boton = tk.Button(root, text="Operacion AND", command=funcion).grid(row=6, column=0)
boton = tk.Button(root, text="Operacion OR", command=funcion).grid(row=6, column=1)
boton = tk.Button(root, text="Operacion NOT", command=funcion).grid(row=6, column=2)


boton = tk.Button(root, text="Histograma", command=lambda:funcion(12,"12") ).grid(row=7, column=0)
boton = tk.Button(root, text="Desplazamiento del Histograma", command= deslpazamientoH ).grid(row=7, column=1)
boton = tk.Button(root, text="Contraccion del Histograma", command= contraccionH ).grid(row=7, column=2)
boton = tk.Button(root, text="Expansion del Histograma", command=lambda:funcion(15,"0", "255") ).grid(row=7, column=3)

boton = tk.Button(root, text="Filtro Mediana", command=lambda:funcion(16,"16")).grid(row=8, column=0)
boton = tk.Button(root, text="Filtro Moda", command=lambda:funcion(17,"17")).grid(row=8, column=1)
boton = tk.Button(root, text="Filtro Media", command=lambda:funcion(18,"18")).grid(row=8, column=2)

boton = tk.Button(root, text="Morfologia Dilatacion", command=lambda:funcion(19,"19")).grid(row=9, column=0)
boton = tk.Button(root, text="Erosion", command=lambda:funcion(20,"20")).grid(row=9, column=1)
boton = tk.Button(root, text="Contorno", command=lambda:funcion(21,"21")).grid(row=9, column=2)
boton = tk.Button(root, text="Apertura", command=lambda:funcion(22,"22")).grid(row=9, column=3)
boton = tk.Button(root, text="Cierre", command=lambda:funcion(23,"23")).grid(row=9, column=4)


boton = tk.Button(root, text="Restaurar", command=restaurar).grid(row=12, column=0)
boton = tk.Button(root, text="Abrir", command=abrir).grid(row=12, column=1)

#canvas.pack(fill="both", expand=True)
'''
boton = tk.Button(root, text="Ruido", command=funcion).grid(row=0, column=0)


boton2 = tk.Button(root, text="RGB y binarizacion", command=win2).pack(side=tk.LEFT)
boton2 = tk.Button(root, text="Operaciones", command=win2).pack(side=tk.LEFT)
boton2 = tk.Button(root, text="Histograma", command=win2).pack(side=tk.LEFT)
boton2 = tk.Button(root, text="Desplazamiento del histograma", command=win2).pack(side=tk.BOTTOM)
boton2 = tk.Button(root, text="Contraccion del histograma", command=win2).pack(side=tk.BOTTOM)
boton2 = tk.Button(root, text="Ex   imgF.close()
pansion del histograma", command=win2).pack(side=tk.BOTTOM)
'''
root.mainloop()