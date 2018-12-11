from PIL import Image
import Operaciones
import matplotlib.pyplot as plt
import time
import numpy as np
'''
def crearMat(data,size):
    matriz = []
    c = 0
    for i in range (size[0]) :
        aux = []
        for j in range ( size[1] ) :
            aux.append(data[c])
            c+=1
        matriz.append(aux)
    return matriz
'''
def crearMat(data,size):
    matriz = []
    c = 0
    for i in range (size[1]) :
        aux = []
        for j in range ( size[0] ) :
            aux.append(data[c])
            c+=1
        matriz.append(aux)
    return matriz
def promediar(matriz, size, f):
    datosc = []
    for i in range (size[1]):
        for j in range(size[0]):
          #  pass
            datosc.append(suma(i,j,matriz,size,f)) 
    return datosc

def suma(x,y, matriz, size, f):
    a = []
    ax = x-1
    ay = y -1
    if (ax<0 or ax >= size[1]) or (ay<0 or ay >= size[0]):    
        return 0
    for i in range (ax, ax+3):
        for j in range (ay, ay+3):
            try:
                a.append(matriz[i][j])
            except IndexError:
                pass 
    if f == 0 :
        if(len(a)>0):
            return int(sum(a) / len(a))
        else :
            return 0
    elif f ==  1 :
        return np.bincount(a).argmax()
    elif f ==  2 :
        return int(np.median(a))
    else :
        return matriz[x][y]
    '''
    for i in range (ax, ax+2):
        for j in range (ay, ay+2):
            try:
                
                a.append(matriz[i][j])
            except IndexError:
                pass
    return matriz[x][y]
    if(len(a)>0):
       # print(sum(a) / len(a) )
        return int(sum(a) / len(a))
    else :
        #print(0)
        return 0

    prom = 0
    c = 0
    rx = range (x-1,x+1)
    ry = range(y-1,y+1)
    aux = range (x-1,x+2,1)
    print(len(aux))
    for i in range (x-1,x+2,1):
        for j in range(y-1,y+2,1):
            #prom = prom+ matriz[i][j]
           if (i>=0 and i < size[0]) and (j>=0 and j < size[1]):
                prom = prom+ matriz[i][j]
            #    c = c + 1
    print (int(prom/9))
    return int(prom/9)
    '''

def pasa_bajas_prom(image):
    img = image.convert('L')
    datos = img.getdata()
    matriz = crearMat(datos, img.size)
    datosn = promediar(matriz, img.size, 0)
    imgg  = Image.new( 'L',img.size )
    imgg.putdata(datosn)
    imgg.save("inuse.jpg")
    imgg.show()
    return imgg

def pasa_bajas_moda(image):
    img = image.convert('L')
    datos = img.getdata()
    matriz = crearMat(datos, img.size)
    datosn = promediar(matriz, img.size,1)
    imgg  = Image.new( 'L',img.size )
    imgg.putdata(datosn)
    imgg.save("inuse.jpg")
    imgg.show()
    return imgg
def pasa_bajas_media(image):
    img = image.convert('L')
    datos = img.getdata()
    matriz = crearMat(datos, img.size)
    datosn = promediar(matriz, img.size,2)
    imgg  = Image.new( 'L',img.size )
    imgg.putdata(datosn)
    imgg.save("inuse.jpg")
    imgg.show()
    return imgg
#analisisimagenesescom
#image = Image.open("tile.png")
#image = Image.open("fractal2.png")
#image.show()
#histogramaRGB("snakes.jpg")
#pasa_bajas_moda(image)
#pasa_bajas_prom(image)

    