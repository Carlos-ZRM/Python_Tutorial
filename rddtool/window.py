from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from uno.grafica import graficaVel
from uno.grafica import graficaIpRequest
from uno.grafica import graficaSnmpPkts
from uno.grafica import graficaSnmpResponse
from uno.grafica import graficaUdpErrors
# Define la ventana principal de la aplicación
def ventana(ip):
    raiz = Tk()

    raiz.geometry('500x1000') # anchura x altura


    raiz.configure(bg = 'beige')

    raiz.title('Datos SNMP del agente '+ip)

    graficaVel(ip)
    graficaIpRequest(ip)
    graficaSnmpPkts(ip)
    graficaSnmpResponse(ip)
    graficaUdpErrors(ip)

    img = PhotoImage(file= ip+"_vel.png" )
    img2 = PhotoImage(file= ip+"_IpRequest.png" )
    img3 = PhotoImage(file= ip+"_snmpInPkts.png" )
    img4 = PhotoImage(file= ip+"_snmpResponse.png" )
    img5 = PhotoImage(file= ip+"_udpInErrors.png" )
    Label(raiz, text= 'Velocidad bits').pack()
    Label(raiz, image= img).pack()
    Label(raiz, text= 'IpRequest').pack()
    Label(raiz, image=img2).pack()
    Label(raiz, text= 'SNMPPkts').pack()
    Label(raiz, image=img3).pack()
    Label(raiz, text= 'UDP Datagrams').pack()
    Label(raiz, image=img4).pack()
    Label(raiz, text= 'UDP Errors').pack()
    Label(raiz, image=img5).pack()

    ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)


    raiz.mainloop()


ventana('localhost')