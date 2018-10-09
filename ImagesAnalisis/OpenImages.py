from PIL import Image
from time_series import Plot_Time_Series
import sys

def umbral (top, img):
    datos = list(img.getdata())
    aux =[]
    sum = 0
    img.show()
    print (datos)
    for i in range (len(datos)):
        aux= datos[i]
        sum = 0
        for j in range (len(aux)):
            sum+=aux[j]
        sum=sum/len(aux)
        if sum > top :
            datos[i]=(0,0,0)
        else :
            datos[i]=(255,255,255)
    result = datos
    img.putdata(datos)
    img.save("test.jpg")
    img.show()
    return result

def escala ( img ):
    datos = list(img.getdata())
    aux =[]
    sum = 0
    escala = 0
    img.show()
    print (datos)
    for i in range (len(datos)):
        aux= datos[i]
        sum = 000
        for j in range (len(aux)):
            sum+=aux[j]
        sum=sum/len(aux)
        escala = int (sum*.33 + sum*.5 + sum*.15)
        datos[i]= (escala,escala,escala)
    result = datos
    img.putdata(datos)
    img.save("test.jpg")
    img.show()
    return result

print("Hola")
path = sys.argv[1]
path = "snakes.jpg"
try:
    img = Image.open(path)
    print("Se abrio imagen")
    print (img.histogram())
    escala( img )
    umbral(3/5*255   ,img)
    histograma=Plot_Time_Series()
    histograma.plot_Histograma(img.histogram())

except IOError:
    print("Error")
