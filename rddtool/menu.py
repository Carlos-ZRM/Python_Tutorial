import os
import tkinter as tk
from tkinter import ttk

from uno.HiloObj import HiloObj


class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)

        self.Hilos = {}


        main_window.title("Lista en Tcl/Tk")
        main_window.geometry('500x500')
        self.listbox = tk.Listbox(self)
        self.listbox.pack()

        self.listbox.insert(0, 'Uno')
        self.boton1 = ttk.Button(main_window, text="Agregar Agente",
                                 command=self.dialogAgregar)
        self.boton1.pack()
        self.pack()

    def dialogAgregar(self):
        self.top = tk.Toplevel(main_window)

        tk.Label(self.top, text="Host name").pack()
        self.dIp = tk.Entry(self.top)
        tk.Label(self.top, text="comunidad").pack()
        self.dC = tk.Entry(self.top)

        self.dIp.pack(padx=5)
        self.dC.pack(padx=5)

        b = tk.Button(self.top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        response = os.system("ping -c 1 " + str(self.dIp.get() ))

        if response == 0:
            hilo = HiloObj(args=(str(self.dC.get()) , str(self.dIp.get() ) ), daemon=False)
            hilo.start()

            #self.Hilo[hilo.getIp()] = hilo
            self.listbox.insert(0, "Comunidad: "+self.dC.get()+"  IP:"+self.dIp.get())
      

        self.top.destroy()


main_window = tk.Tk()
app = Application(main_window)
app.mainloop()

"""

hostname = "google.com" #example
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print( hostname, 'is up!')
else:
  print ( hostname, 'is down!')

"""
