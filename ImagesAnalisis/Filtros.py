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
def umbralD (data,datan,  umbral):
    for i in range ( len(data) ):
        inf = umbral[0]
        sup = umbral[1]
        if ( data[i]>inf and  data[i]<sup ):
            datan[i] = -1
def multiU (image, umbrales):
    img = image.convert('L')

    data = img.getdata()
    datan = []
    datar = []
    size = image.size[0]*image.size[1]
    for i in range (size):
        datan.append(0)
    
    for j in range (size):
        aux = []
        aux = umbrales[0]
        umbralD(data, datan, aux )
    for i in range ( len (size)):
        if (datan[i]== -1 ):
            datar.append((255))
        else :
            datar.append((0))
    imgg  = Image.new( 'L',img.size )
    imgg.putdata(datar)
    imgg.save("inuse.jpg")
    imgg.show()
    return imgg

def umbral( image, umbral ):
    img = image.convert('L')
    data = img.getdata()
    datan = []
    data2 = image.getdata()
    datan2 = []
    for i in range ( len(data) ):
        if ( data[i]>umbral[0] and  data[i]<umbral[1] ):
            datan.append( (0) )
            datan2.append( data2[i] )
        else :
            datan.append( (255) )
            datan2.append( (255,255,255) )
    imgg  = Image.new( 'RGB',img.size )
    imgg.putdata(datan2)
    imgg.save("inuse.jpg")
    imgg.show()
    return imgg
"""
def invertir ():
    img = image.convert('L')
    data = img.getdata()
    datan = []
    for i in range (len(data)):
"""

def multiumbral(image , umbrales ):
    
    img = image.convert('L')
    data = img.getdata()
    datan = []
    flag = False

    for i in range ( len(data) ):
        for j in range (len (umbrales) ) :
            umbral = umbrales[j]
           
            if ( data[i]>umbral[0] and  data[i]<umbral[1] ):
                print (umbral)
                print(data[i])
                flag = True
        
        if flag :
            datan.append((255))
        else :
            datan.append ((0))

    imgg  = Image.new( '1',img.size )
    imgg.putdata(datan)
    imgg.save("inuse.jpg")
    imgg.show()
    return imgg
    return
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
#image = Image.open("snakes.jpg")
#image = Image.open("fractal2.png")
#image.show()
#histogramaRGB("snakes.jpg")
#pasa_bajas_moda(image)
#pasa_bajas_prom(image)

image = Image.open("imagenes/pool.png")
image.show()
par = [image, [45,50]]
#aux = umbral(image, [160,180])
da = [[40,49], [25,30]]
aux1 = umbral( image, [25,30] ) 
aux1.save("s1.jpg")
aux2 =  umbral( image, [45,50] ) 
aux2.save("s2.jpg")
aux3 =  umbral( image, [15,20] ) 
aux3.save("s3.jpg")
res = Operaciones.suma(aux1,aux2)
res.show()