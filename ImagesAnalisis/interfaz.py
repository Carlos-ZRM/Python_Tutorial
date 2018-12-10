import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

def Cerrar():
    pass
def funcion():
   print ("Excelente")
def win2():
    tl = tk.Toplevel(root)
    tl.title("Modificar Datos")
    tl.geometry('100x100')
    tl.focus_set()
    tl.grab_set()
    tl.transient(master=root)

    inf = tk.StringVar(tl)
    entry1 = tk.Entry(tl, textvariable=inf)
    entry1.grid(row=0, column=1)
    label1 = tk.Label(tl, text='Hija', bg="red")
    label1.grid(row=0, column=0)
    b = tk.Button(tl,text="Cerrar",bg="green", command=cerrar)

    b.pack()


root = tk.Tk()

pic = "snakes.jpg"
img = Image.open(pic)

o_size = img.size   #Tamaño original de la imagen
f_size = (img.size) #Tamaño del canvas donde se mostrará la imagen

'''
factor = min(float(f_size[1])/o_size[1], float(f_size[0])/o_size[0])
width = int(o_size[0] * factor)
height = int(o_size[1] * factor)

rImg= img.resize((width, height), Image.ANTIALIAS)
'''
img2 = ImageTk.PhotoImage(img)

canvas = tk.Canvas(root, width=f_size[0], height= f_size[1])
canvas.create_image(f_size[0]/2, f_size[1]/2, anchor=tk.CENTER, image=img2, tags="img")
canvas.pack(fill=None, expand=False)

boton = tk.Button(root, text="Que te parece la guía?", command=funcion)
boton.pack()

boton2 = tk.Button(root, text="Abrir", command=win2).pack()
root.mainloop()