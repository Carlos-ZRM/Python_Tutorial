from PIL import Image
from random import uniform
import Operaciones
import matplotlib.pyplot as plt

def contraccion(datos, k, minimo, cminimo ):
   datar = []
   for i in range(len(datos)):
      tupla = datos[i]
      aux = k*(tupla-minimo)+cminimo
      if  aux>254:
         r = 255
      elif aux<1:
         r = 0
      else :
         r = aux
      datar.append((r))
   return datar
def suma (data1,data2):
   datar=[]
   for i in range(len(data1)):
      tupla1 = data1[i]
      tupla2 = data2[i]
      r = tupla1[0]+tupla2[0] if tupla1[0]+tupla2[0]<255 else 255
      g = tupla1[1]+tupla2[1] if tupla1[1]+tupla2[1]<255 else 255
      b = tupla1[2]+tupla2[2] if tupla1[2]+tupla2[2]<255 else 255
      datar.append((r,g,b))
   return datar
def restaCte (data1,cte):
   datar=[]
   for i in range(len(data1)):
      tupla1 = data1[i]
      if  tupla1+cte>254:
         r = 255
      elif tupla1+cte<1:
         r = 0
      else :
         r = tupla1+cte
      datar.append((r))
   return datar
def resta (data1,data2):
   datar=[]
   for i in range(len(data1)):
      tupla1 = data1[i]
      tupla2 = data2[i]
      r = tupla1[0]-tupla2[0] if tupla1[0]-tupla2[0]>0 else 0
      g = tupla1[1]-tupla2[1] if tupla1[1]-tupla2[1]>0 else 0
      b = tupla1[2]-tupla2[2] if tupla1[2]-tupla2[2]>0 else 0
      datar.append((r,g,b))
   return datar

def restaIMG (img1,img2):
   data1 = img1.getdata()
   data2 = img2.getdata()
   datar=[]
   g = 0
   for i in range(len(data1)):
      tupla1 = data1[i]
      tupla2 = data2[i]
      g = tupla1-tupla2 if tupla1-tupla2>0 else 0
      datar.append(g)
   imgg  = Image.new( 'L',img1.size )
   imgg.putdata(datar)
   imgg.save("hist-escala-desplazamiento.jpg")
   return imgg
def and_img (data1,data2) :
   datar = []
   for i in range (len(data1)):
      datar.append( data1[i] and data2[i])
   return datar
def or_img (data1,data2) :
   datar = []
   for i in range (len(data1)):
      datar.append( data1[i] or data2[i])
   return datar
def xor_img (data1,data2) :
   datar = []
   for i in range (len(data1)):
      datar.append( data1[i] ^ data2[i])
   return datar
def not_img (data) :
   datar = []
   for i in range (len(data)):
      datar.append(255 - data[i])
   return datar
def not_rgb (data) :
   datar = []
   for i in range (len(data)):
      tupla = data[i]
      r =255 - tupla[0] if 255 -tupla[1]>0 else 0
      g =255 - tupla[1] if 255 -tupla[1]>0 else 0
      b =255 - tupla[1] if 255 -tupla[1]>0 else 0
      datar.append((r,g,b))
   return datar

img = Image.open("snakes.jpg").convert('L')
datos = img.getdata()
datosn = not_img(datos)
imgg  = Image.new( 'L',img.size )
imgg.putdata(datosn)
imgg.show()
imgg.save("Nueva.jpg")
img = Image.open("snakes.jpg")
imgg  = Image.new( "RGB",img.size )
datos = img.getdata()
datosn = not_rgb(datos)
imgg.putdata(datosn)
imgg.show()
imgg.save("Nuevas.jpg")