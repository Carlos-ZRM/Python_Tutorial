from PIL import Image
from random import uniform
import Operaciones
import matplotlib.pyplot as plt

def additivo (img, valor):
    img = image.convert('L')
    datos = img.getdata()
    datosn = []
    for i in range (len (datos)):
        r = uniform(0,1)
        if (r <=  valor ):
            datosn.append((0))
        else :
            datosn.append(datos[i])
    imgg  = Image.new( 'L',img.size )
    imgg.putdata(datosn)
    imgg.save("ruidoAdd.jpg")
    imgg.show()
def sustractivo (img, valor):
    img = image.convert('L')
    datos = img.getdata()
    datosn = []
    for i in range (len (datos)):
        r = uniform(0,1)
        if (r <=  valor ):
            datosn.append((255))
        else :
            datosn.append(datos[i])
    imgg  = Image.new( 'L',img.size )
    imgg.putdata(datosn)
    imgg.save("ruidoAdd.jpg")
    imgg.show()

def pimienta (img, valor):
    img = image.convert('L')
    datos = img.getdata()
    datosn = []
    for i in range (len (datos)):
        r = uniform(0,1)
        if (r <  valor/2 ):
            datosn.append((255))
        elif (r<= valor):
            datosn.append((0))
        else :
            datosn.append(datos[i])
    imgg  = Image.new( 'L',img.size )
    imgg.putdata(datosn)
    imgg.save("ruidoAdd.jpg")
    imgg.show()


image = Image.open("snakes.jpg")
sustractivo(image,.1)
additivo(image,.1)
pimienta(image,.2)
    
