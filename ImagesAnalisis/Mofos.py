from PIL import Image
import Operaciones
import matplotlib.pyplot as plt
import time
import numpy as np

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
def creardata (matrizb, size):
    a = []
    for x in range (size[1]):
        for y in range(size[0]):
            a.append(matrizb[x][y])
    return a

def erosionar(x, y , matriza, matrizb, tile, size):
    ax = x-1
    ay = y -1
    xx = 0
    yy = 0
    flag = True
    for i in range (ax, ax+3):
        for j in range (ay, ay+3):
            if (i<0 or i >= size[1]) or (j<0 or j >= size[0]):
                continue
            if tile[xx][yy] is -1:
                continue
            if tile[xx][yy] != matriza [i][j]  :
               flag = False
               #matrizb[x][y] = 255
        yy = yy + 1
    xx = xx + 1
    #print(flag)
    if flag:
        matrizb[x][y] = 0
    else :
        for i in range (ax, ax+3):
            for j in range (ay, ay+3):
                if (i<0 or i >= size[1]) or (j<0 or j >= size[0]):
                    continue
                matrizb[i][j] = 255
    return 
def dilatar(x, y , matriza, matrizb, tile, size):
    ax = x-1
    ay = y -1
    xx = 0
    yy = 0
    if (matriza[x][y] != tile[1][1]):
        return
    for i in range (ax, ax+3):
        for j in range (ay, ay+3):
            #print(str(i)+", "+str(j))
            if (i<0 or i >= size[1]) or (j<0 or j >= size[0]):
                continue
            if tile[xx][yy] == 0 :
                    matrizb [i][j] = 0
        yy = yy + 1
    xx = xx + 1
            #if tile[xx][yy] is 0 :
            #    matrizb [ax][ay] = 0
def recorrer (matriza, matrizb, tile, size, op):
    for x in range (size[1]):
        for y in range(size[0]):
            if op == 0:
                dilatar(x, y , matriza, matrizb, tile, size)
            elif op == 1 :
                erosionar(x, y , matriza, matrizb, tile, size)
    return 
def dilatacion(image):
    img = image.convert('1')
    datos = img.getdata()
    datosb = img.getdata()
    matriza = crearMat(datos, img.size)
    matrizb = crearMat(datos, img.size)

    #tile =  np.matrix('-1 1 -1;1 1 1; -1 1 -1')
    tile = [[-1,0,-1],[0,0,-1],[-1,-1,-1]]
    #tile = [[0,0,0],[0,0,0],[0,0,0]]
    print(tile)
    #print(matrizb)
    recorrer(matriza, matrizb, tile, img.size, 0 )
    datosn = creardata(matrizb, img.size)
    imgg  = Image.new( 'L',img.size )
    imgg.putdata(datosn)
    imgg.save("inuse.jpg")
    imgg.show()
    return imgg

def erosion(image):
    img = image.convert('1')
    datos = img.getdata()
    datosb = img.getdata()
    matriza = crearMat(datos, img.size)
    matrizb = crearMat(datos, img.size)
    tile = [[-1,0,-1],[0,0,-1],[-1,-1,-1]]

    #tile =  np.matrix('-1 1 -1;1 1 1; -1 1 -1')
    #tile = [[0,-1,-1],[-1,0,-1],[-1,-1,0]]
    #tile = [[0,0,0],[0,0,0],[0,0,0]]
    print(tile)
    #print(matrizb)
    recorrer(matriza, matrizb, tile, img.size,1)
    datosn = creardata(matrizb, img.size)
    imgg  = Image.new( '1',img.size )
    imgg.putdata(datosn)
    imgg.save("inuse.jpg")
    imgg.show()
    return imgg
def contorno (image):
    aux = erosion(image)
    aux2 = erosion(aux)
    frontera = Operaciones.restaIMG(aux,image)
    return frontera

'''
#image = Image.open("fractal.png")
#image = Image.open("fractal2.png")
image = Image.open("test2.jpg")
image = Image.open("snakes.jpg")

#histogramaRGB("snakes.jpg")
image.show()
aux = erosion(image)
aux2 = erosion(aux)
frontera = Operaciones.restaIMG(aux,image)
frontera.show()
#dilatacion(aux)
aux = erosion(image)
aux.show()
image = Image.open("test2.jpg")

'''

#image = Image.open("snakes.jpg")
