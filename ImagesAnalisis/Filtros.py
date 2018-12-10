from PIL import Image
import Operaciones
import matplotlib.pyplot as plt
import time
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
    for i in range (size[0]) :
        aux = []
        for j in range ( size[1] ) :
            aux.append(data[c])
            c+=1
        matriz.append(aux)
    return matriz
def promediar(matriz, size):
    datosc = []
    for i in range (size[0]):
        for j in range(size[1]):
          #  pass
           datosc.append(suma(i,j,matriz,size)) 
    return datosc

def suma(x,y, matriz, size):
    ax = x-1
    ay = y -1
    lista = []
    for i in range (ax, ax+3):
        for j in range (ay, ay+3):
            
    '''
    prom = 0.0 
    c = 0
    ax = x-1
    ay = y -1 
    for i in range (ax, ax+3):
        for j in range (ay, ay+3):
            try:
                if (i>=0 and j>=0):
                    time.sleep(.01) 
                    print(str(i)+" , "+str(j))
                    prom = prom+ matriz[i][j]
                    c = c+1
            except IndexError:
                prom = prom
    
    return int (prom/c)
    
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

def pasa_bajas_prom(img):
    img = image.convert('L')
    datos = img.getdata()
    print (img.size)
    matriz = crearMat(datos, img.size)
    datosn = promediar(matriz, img.size)
    imgg  = Image.new( 'L',img.size )
    imgg.putdata(datosn)
    imgg.save("filtro-promedio.jpg")
    imgg.show()

#analisisimagenesescom
#image = Image.open("tile.png")
image = Image.open("snakes.jpg")
#image.show()
#histogramaRGB("snakes.jpg")
pasa_bajas_prom(image)


    