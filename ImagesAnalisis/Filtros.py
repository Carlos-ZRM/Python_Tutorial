from PIL import Image
import Operaciones
import matplotlib.pyplot as plt

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
         datosc.append(suma(i,j,matriz,size))
    return datosc

def suma(x,y, matriz, size):
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

def pasa_bajas_prom(img):
    img = image.convert('L')
    datos = img.getdata()
    matriz = crearMat(datos, img.size)
    datosn = promediar(matriz, img.size)
    imgg  = Image.new( 'L',img.size )
    imgg.putdata(datosn)
    imgg.save("filtro-promedio.jpg")
    imgg.show()



#image = Image.open("tile.png")
image = Image.open("snakes.jpg")
image.show()
#histogramaRGB("snakes.jpg")
pasa_bajas_prom(image)


    