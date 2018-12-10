from PIL import Image
from time_series import Plot_Time_Series
import Operaciones
import sys

class Umbral :
    def __init__(self):
        self.Historial=[]
        self.maxHist=5
        self.xHist=-1
    def addHistorial( self, elemento):
        if len(self.Historial) < self.maxHist :
            self.Historial.append(elemento)
            self.xHist += 1
        else :
            if self.xHist == self.maxHist-1 :
                self.xHist = 0
                self.Historial[self.xHist]=elemento
            else :
                self.xHist += 1
                self.Historial[self.xHist]=elemento
        return
    def removeHistorial( self ):
        if  len(self.Historial) < self.maxHist :
            self.Historia.remove(self.xHist)
            self.xHist -= 1
        else :
            self.xHist -= 1
        return

    def escala ( self, img ):
        datos = list(img.getdata())
        aux =[]
        sum = 0
        escala = 0
        for i in range (len(datos)):
            aux= datos[i]
            sum = 000
            for j in range (len(aux)):
                sum+=aux[j]
            sum=sum/len(aux)
            escala = int (sum*.33 + sum*.5 + sum*.15)
            datos[i]= (escala,escala,escala)        
        imgr  = Image.new('RGB', img.size )
        imgr.putdata(datos)
        imgr.save("inuse.jpg")
        imgr.show()
        return imgr

    def rgb(self, img, op):
        datosr=[]
        datosg=[]
        datosb=[]
        datos = list(img.getdata())
        aux=[]
        dimensiones = img.size
        for i in range(len(datos)):
            aux=datos[i]
            datosr.append((aux[0],0,0))
            datosg.append((0,aux[1],0))
            datosb.append((0,0,aux[2]))
        imgr  = Image.new('RGB', dimensiones )
        imgr.putdata(datosr)
        imgr.save("imagenr.jpg")
        
        imgg  = Image.new( 'RGB',dimensiones )
        imgg.putdata(datosg)
        imgg.save("imageng.jpg")
        
        imgb  = Image.new( 'RGB',dimensiones )
        imgb.putdata(datosb)
        imgb.save("imagenb.jpg")

        imgr.show()
        imgg.show()
        imgb.show()

        '''
        datar = Operaciones.resta(datos,datosb)
        imgs  = Image.new( 'RGB',dimensiones )
        imgs.putdata(datar)
        imgs.save("imagens.jpg")
        imgs.show()
        histograma=Plot_Time_Series()
        histograma.plot_Histograma(imgs.histogram())
        '''
        if op == 'r':
            imgr.save("inuse.jpg")
            return imgr
        elif op == 'g':
            imgg.save("inuse.jpg")
            return imgg
        else :
            imgb.save("inuse.jpg")
            return imgb

    def umbral ( self, top, img):
        datos = list(self.Historial[self.xHist].getdata() )
        aux = []
        sum = 0

        for i in range (len(datos)):
            aux= datos[i]
            sum = 0
            for j in range (len(aux)):
                sum+=aux[j]
            sum=sum/len(aux)
            if sum > top :
                #datos[i]=(0,0,0)
                datos[i]=0
            else :
                #datos[i]=(255,255,255)
                datos[i]=1
        dimensiones = self.Historial[self.xHist].size
        img2  = Image.new('1', dimensiones )
        img2.putdata(datos)
        #print( datos)
        img2.save("inuse.jpg")
        img2.show()
        self.addHistorial( img2)
        return img2
    
'''
print("Hola")
op = OpenImages()

path = sys.argv[1]
path = "snakes.jpg"
try:
    img = Image.open(path)
    print("Se abrio imagen")
    op.addHistorial(img)
    img.show()
    op.rgb(img)
    #print (img.histogram())
    #op.escala( img )
    #op.umbral(3/5*255   ,img)
    histograma=Plot_Time_Series()
    histograma.plot_Histograma(img.histogram())

except IOError:
    print("Error")
'''